Param(
    [string]$ProjectName = 'backend',
    [string]$AppName = 'school',
    [string]$EnvFile = '.env',
    [string]$SqlFile = 'shahania_full_ddl_v1.sql'
)

$ErrorActionPreference = 'Stop'

function Write-Info($msg){ Write-Host "[INFO] $msg" -ForegroundColor Cyan }
function Write-OK($msg){ Write-Host "[OK]   $msg" -ForegroundColor Green }
function Write-Warn($msg){ Write-Host "[WARN] $msg" -ForegroundColor Yellow }
function Write-Err($msg){ Write-Host "[ERR]  $msg" -ForegroundColor Red }

# 1) Ensure Python available
Write-Info 'Checking Python availability...'
$py = (Get-Command python -ErrorAction SilentlyContinue)
if(-not $py){ Write-Err 'Python not found in PATH'; exit 1 }
Write-OK ("Python: " + (python --version))

# 2) Ensure virtual env .venv exists and activated (optional)
if(-not (Test-Path '.venv')){
  Write-Info 'Creating virtual environment (.venv)'
  python -m venv .venv
}
Write-OK 'Virtual environment ready (.venv)'

# 3) Install deps
Write-Info 'Installing Django & database drivers & dotenv'
& .\.venv\Scripts\python -m pip install --upgrade pip > $null
& .\.venv\Scripts\pip install django psycopg2-binary python-dotenv > $null
Write-OK 'Dependencies installed'

# 4) Create Django project if not exists
if(-not (Test-Path $ProjectName)){
  Write-Info "Creating Django project: $ProjectName"
  & .\.venv\Scripts\django-admin startproject $ProjectName .
  Write-OK 'Project created'
} else { Write-Warn "Project folder '$ProjectName' already exists. Skipping." }

# 5) Create app if not exists
if(-not (Test-Path $AppName)){
  Write-Info "Creating Django app: $AppName"
  & .\.venv\Scripts\python manage.py startapp $AppName
  Write-OK 'App created'
} else { Write-Warn "App '$AppName' already exists. Skipping." }

# 6) Write .env example if not exists
if(-not (Test-Path '.env')){
$envContent = @'
DJANGO_SETTINGS_MODULE=backend.settings
SECRET_KEY=change-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
PG_NAME=shahania_db
PG_USER=sh_user
PG_PASSWORD=09041974
PG_HOST=127.0.0.1
PG_PORT=5432
REDIS_URL=redis://127.0.0.1:6379/0
'@
  Set-Content -Path $EnvFile -Value $envContent -Encoding UTF8
  Write-OK ".env written"
} else { Write-Warn ".env already exists. Skipping write." }

# 7) Patch settings.py to load .env and configure DB + Arabic locale
$settingsPath = Join-Path $ProjectName 'settings.py'
if(Test-Path $settingsPath){
  $settings = Get-Content $settingsPath -Raw
  if(-not ($settings -match 'from dotenv import load_dotenv')){
    $settings = $settings -replace 'from pathlib import Path',[string]"from pathlib import Path`nimport os`nfrom dotenv import load_dotenv"
  }
  if(-not ($settings -match 'load_dotenv')){
    $settings = $settings -replace '(BASE_DIR = .*?\n)','${0}load_dotenv(BASE_DIR / ".env")`n'
  }
  # Inject LANGUAGE_CODE, TIME_ZONE, ALLOWED_HOSTS parsing
  $settings = $settings -replace 'LANGUAGE_CODE = .*','LANGUAGE_CODE = "ar"'
  $settings = $settings -replace 'TIME_ZONE = .*','TIME_ZONE = "Asia/Qatar"'
  if($settings -notmatch 'ALLOWED_HOSTS ='){
    $settings = $settings -replace 'DEBUG = .*','DEBUG = os.getenv("DEBUG","False") == "True"`nALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS","127.0.0.1,localhost").split(",") if h.strip()]'
  } else {
    $settings = $settings -replace 'ALLOWED_HOSTS = .*','ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS","127.0.0.1,localhost").split(",") if h.strip()]'
  }
  # Install app in INSTALLED_APPS if missing
  if($settings -notmatch "'$AppName'"){
    $settings = $settings -replace '(INSTALLED_APPS = \[)',"$1`n    '$AppName',"
  }
  # Configure DATABASES entirely
  $dbBlock = @'
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("PG_NAME"),
        "USER": os.getenv("PG_USER"),
        "PASSWORD": os.getenv("PG_PASSWORD"),
        "HOST": os.getenv("PG_HOST", "127.0.0.1"),
        "PORT": os.getenv("PG_PORT", "5432"),
    }
}
'@
  $settings = $settings -replace 'DATABASES = \{[\s\S]*?\}\n',$dbBlock
  Set-Content -Path $settingsPath -Value $settings -Encoding UTF8
  Write-OK 'settings.py updated'
}

# 8) Migrate Django core tables (creates auth_user)
Write-Info 'Running Django migrations (auth, sessions, etc.)'
& .\.venv\Scripts\python manage.py migrate
Write-OK 'Core migrations completed'

# 9) (Optional) Load DDL file into database if file exists and psql available
if(Test-Path $SqlFile){
  Write-Info "Found SQL file '$SqlFile'. Attempting to load via psql..."
  $psql = (Get-Command psql -ErrorAction SilentlyContinue)
  if($psql){
    $pgdb = (Get-Content $EnvFile | Where-Object { $_ -match '^PG_NAME=' }) -replace 'PG_NAME=',''
    $pguser = (Get-Content $EnvFile | Where-Object { $_ -match '^PG_USER=' }) -replace 'PG_USER=',''
    $pghost = (Get-Content $EnvFile | Where-Object { $_ -match '^PG_HOST=' }) -replace 'PG_HOST=','127.0.0.1'
    $pgport = (Get-Content $EnvFile | Where-Object { $_ -match '^PG_PORT=' }) -replace 'PG_PORT=','5432'
    Write-Warn 'If psql prompts for password, use PG_PASSWORD from .env.'
    & psql -h $pghost -p $pgport -U $pguser -d $pgdb -f $SqlFile
    Write-OK 'DDL executed (if no errors reported)'
  } else {
    Write-Warn 'psql not found. Skipping automatic DDL import.'
  }
} else {
  Write-Warn "SQL file '$SqlFile' not found. Skipping DDL import."
}

# 10) Reverse engineer DB into models.py via inspectdb
Write-Info 'Generating models from database (inspectdb)'
& .\.venv\Scripts\python manage.py inspectdb > (Join-Path $AppName 'models.py')
Write-OK "Models generated at ./$AppName/models.py"

# 11) Create admin.py that auto-registers all non-abstract models
$adminPath = Join-Path $AppName 'admin.py'
$adminContent = @'
from django.contrib import admin
from . import models

# تسجيل تلقائي لجميع النماذج غير المجردة
for name in dir(models):
    obj = getattr(models, name)
    try:
        if hasattr(obj, "_meta") and getattr(obj._meta, "abstract", False) is False:
            admin.site.register(obj)
    except admin.sites.AlreadyRegistered:
        pass
'@
Set-Content -Path $adminPath -Value $adminContent -Encoding UTF8
Write-OK "Admin configured at ./$AppName/admin.py"

# 12) Done
Write-OK 'Backend bootstrap finished. Next steps:'
Write-Host '  - Create superuser: ./.venv/Scripts/python manage.py createsuperuser' -ForegroundColor Gray
Write-Host '  - Run server:      ./.venv/Scripts/python manage.py runserver' -ForegroundColor Gray

Param()

# ==========
# Utilities
# ==========
function Write-Section($title) {
  Write-Host ""
  Write-Host "== $title ==" -ForegroundColor Cyan
}

function Run-PyBlock {
  param([Parameter(Mandatory=$true)][string]$Code)

  # استخدم بايثون الخاص بالبيئة الحالية (تأكد أنك فعّلت .venv قبل تشغيل السكربت)
  $py = "python"
  # أنشئ ملف مؤقت
  $tmp = [System.IO.Path]::GetTempFileName()
  $pyFile = [System.IO.Path]::ChangeExtension($tmp, ".py")
  Set-Content -Path $pyFile -Value $Code -Encoding UTF8

  & $py $pyFile

  Remove-Item -Force $pyFile, $tmp -ErrorAction SilentlyContinue
}

# ==========
# Checks
# ==========
Write-Section "التحقق من البيئة"
python -c "import sys; print(sys.executable)"

Write-Section "Django check"
python manage.py check

Write-Section "URLConf/Deploy Checks"
python manage.py check --deploy

Write-Section "استيراد نماذج كل التطبيقات"
Run-PyBlock @'
import importlib
apps = ["apps.core","apps.people","apps.timetable","apps.attendance","apps.assessment","apps.behavior","apps.health","apps.transport","apps.library","apps.refdata","apps.identity"]
for a in apps:
    try:
        importlib.import_module(a + ".models")
        print(f"[OK] {a}.models")
    except Exception as e:
        print(f"[FAIL] {a}.models -> {e}")
'@

Write-Section "الهجرات"
python manage.py showmigrations

Write-Section "خطة الهجرات"
python manage.py migrate --plan

Write-Section "فحص Ruff/Pyflakes"
try { .\.venv\Scripts\python.exe -m ruff --version; .\.venv\Scripts\python.exe -m ruff check apps } catch { Write-Warning "Ruff غير مثبت في هذه البيئة" }
try { .\.venv\Scripts\python.exe -m pyflakes --version; .\.venv\Scripts\python.exe -m pyflakes apps } catch { Write-Warning "Pyflakes غير مثبت في هذه البيئة" }

Write-Host "`n[✔] الفحوصات اكتملت." -ForegroundColor Green
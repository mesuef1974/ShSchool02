cd D:\ShSchool02\backend
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force

@'
Param(
  [Parameter(Mandatory=$false)][string]$PatchRoot = "",
  [Parameter(Mandatory=$false)][string]$ProjectRoot = "",
  [switch]$DryRun,
  [switch]$NoBackup
)

# ==============================================
# Shahania – PowerShell Patcher (v0.2, v2 fix)
#  - يصلّح شرط Test-Path مع -and
#  - في وضع DryRun يعرض "Would copy" بدل "Copied"
# ==============================================

function Write-Step($msg){ Write-Host ("[+] {0}" -f $msg) -ForegroundColor Cyan }
function Write-OK($msg){ Write-Host ("[✓] {0}" -f $msg) -ForegroundColor Green }
function Write-Warn($msg){ Write-Warning $msg }
function Write-Err($msg){ Write-Host ("[X] {0}" -f $msg) -ForegroundColor Red }

# 1) تحديد المسارات
if (-not $PatchRoot -or $PatchRoot.Trim() -eq "") {
  $maybe = Resolve-Path ".\shahania_i18n_str_patch_v0_2" -ErrorAction SilentlyContinue
  if ($maybe) { $PatchRoot = $maybe.ProviderPath } else { $PatchRoot = (Resolve-Path ".").ProviderPath }
}
if (-not $ProjectRoot -or $ProjectRoot.Trim() -eq "") {
  $ProjectRoot = (Resolve-Path ".").ProviderPath
}

Write-Step "PatchRoot = $PatchRoot"
Write-Step "ProjectRoot = $ProjectRoot"

# 2) التحقق من بنية المجلدات
$apps = @('core','people','timetable','attendance','assessment','behavior','health','transport','library','refdata','identity')
$srcAppsRoot = Join-Path $PatchRoot 'apps'
$dstAppsRoot = Join-Path $ProjectRoot 'apps'

if (-not (Test-Path -Path $srcAppsRoot)) { Write-Err "لم يتم العثور على مجلد apps داخل PatchRoot: $srcAppsRoot"; exit 1 }
if (-not (Test-Path -Path $dstAppsRoot)) { Write-Err "لم يتم العثور على مجلد apps داخل مشروعك: $dstAppsRoot"; exit 1 }

# 3) وظيفة نسخ مع نسخة احتياطية
function Copy-WithBackup($src,$dst){
  $dstDir = Split-Path $dst -Parent
  if (-not (Test-Path -Path $dstDir)) { New-Item -ItemType Directory -Force -Path $dstDir | Out-Null }

  if ((Test-Path -Path $dst) -and (-not $NoBackup)) {
    $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $bak = "$dst.$stamp.bak"
    if ($DryRun) {
      Write-Step "(DryRun) Would backup: $(Split-Path -Leaf $dst) → $(Split-Path -Leaf $bak)"
    } else {
      Copy-Item -Path $dst -Destination $bak -Force
      Write-Step "Backup: $(Split-Path -Leaf $dst) → $(Split-Path -Leaf $bak)"
    }
  }

  if ($DryRun) {
    Write-OK "(DryRun) Would copy: $(Split-Path -Leaf $src) → $dst"
  } else {
    Copy-Item -Path $src -Destination $dst -Force
    Write-OK "Copied: $(Split-Path -Leaf $src) → $dst"
  }
}

# 4) نسخ ملفات models.py و apps.py لكل تطبيق
foreach ($app in $apps) {
  $srcApp = Join-Path $srcAppsRoot $app
  $dstApp = Join-Path $dstAppsRoot $app
  if (-not (Test-Path -Path $srcApp)) { Write-Warn "المجلد غير موجود في الباتش: $srcApp"; continue }
  if (-not (Test-Path -Path $dstApp)) { Write-Warn "تطبيق غير موجود في مشروعك: $dstApp"; continue }

  foreach ($file in @('models.py','apps.py')) {
    $src = Join-Path $srcApp $file
    $dst = Join-Path $dstApp $file
    if (Test-Path -Path $src) { Copy-WithBackup $src $dst } else { Write-Warn "لا يوجد $file في $srcApp" }
  }
}

# 5) backend_admin_header.py (اختياري)
$srcHeader = Join-Path $PatchRoot 'backend_admin_header.py'
if (Test-Path -Path $srcHeader) {
  $dstHeader = Join-Path $ProjectRoot 'backend_admin_header.py'
  Copy-WithBackup $srcHeader $dstHeader
  Write-OK "أضفت/سأضيف ملف تخصيص عناوين لوحة الإدارة (اختياري). لا تنس إضافة: 'import backend_admin_header' في backend/urls.py"
}
else { Write-Warn "backend_admin_header.py غير موجود في PatchRoot" }

Write-Host "`n[إرشاد] عدّل INSTALLED_APPS في backend/settings.py لاستخدام AppConfig لكل تطبيق (مثال: 'apps.core.apps.CoreConfig')." -ForegroundColor Yellow
Write-Host "[✔] انتهى التنفيذ." -ForegroundColor Cyan
'@ | Set-Content -Encoding UTF8 .\scripts\patch_admin_i18n_v2.ps1
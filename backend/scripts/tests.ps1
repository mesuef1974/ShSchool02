Param(
    [string]$HostUrl = "http://127.0.0.1:8000",
    [string]$Username,
    [SecureString]$Password
)

# =============================
#  Script: tests.ps1 (Shahania v0.2)
#  الغرض: اختبار مصادقة JWT واستدعاء بعض واجهات الـ API
#  اللغة: العربية
# =============================

function ConvertFrom-SecureStringToPlainText {
    param([Parameter(Mandatory=$true)][SecureString]$Secure)
    $bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($Secure)
    try { return [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr) }
    finally { [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr) }
}

Write-Host "[+] بدء اختبار واجهات Shahania API على: $HostUrl" -ForegroundColor Cyan

# 1) جمع بيانات الدخول
if (-not $Username) {
    $Username = Read-Host "اسم المستخدم (مثال: admin)"
}
if (-not $Password) {
    $Password = Read-Host "كلمة المرور" -AsSecureString
}
$PlainPassword = ConvertFrom-SecureStringToPlainText -Secure $Password

# 2) إصدار توكن (access/refresh)
try {
    $loginBody = @{ username = $Username; password = $PlainPassword } | ConvertTo-Json
    $tokenResp = Invoke-RestMethod -Method POST -Uri "$HostUrl/api/auth/token/" -Headers @{"Content-Type"="application/json"} -Body $loginBody
    $access  = $tokenResp.access
    $refresh = $tokenResp.refresh
    if (-not $access) { throw "لم يتم استلام access token" }
    Write-Host "[+] تم إصدار التوكن بنجاح" -ForegroundColor Green
}
catch {
    Write-Error "[X] فشل إصدار التوكن: $($_.Exception.Message)"
    if ($_.ErrorDetails.Message) { Write-Host $_.ErrorDetails.Message }
    exit 1
}

# 3) دالة مساعدة لاستدعاء GET
function Invoke-ApiGet {
    param([Parameter(Mandatory=$true)][string]$Path)
    try {
        $resp = Invoke-RestMethod -Method GET -Uri ("{0}{1}" -f $HostUrl, $Path) -Headers @{"Authorization" = "Bearer $access"}
        return $resp
    }
    catch {
        Write-Error "[X] فشل استدعاء $Path : $($_.Exception.Message)"
        if ($_.ErrorDetails.Message) { Write-Host $_.ErrorDetails.Message }
        return $null
    }
}

# 4) أمثلة استدعاءات
$students = Invoke-ApiGet -Path "/api/students/"
if ($students -ne $null) {
    Write-Host "[✓] /api/students/" -ForegroundColor Green
    $students | ConvertTo-Json -Depth 6 | Write-Output
}

$attendance = Invoke-ApiGet -Path "/api/attendance-records/"
if ($attendance -ne $null) {
    Write-Host "[✓] /api/attendance-records/" -ForegroundColor Green
    $attendance | ConvertTo-Json -Depth 6 | Write-Output
}

$exams = Invoke-ApiGet -Path "/api/exams/"
if ($exams -ne $null) {
    Write-Host "[✓] /api/exams/" -ForegroundColor Green
    $exams | ConvertTo-Json -Depth 6 | Write-Output
}

# 5) تحديث التوكن عبر refresh (اختياري)
try {
    $refreshBody = @{ refresh = $refresh } | ConvertTo-Json
    $refResp = Invoke-RestMethod -Method POST -Uri "$HostUrl/api/auth/token/refresh/" -Headers @{"Content-Type"="application/json"} -Body $refreshBody
    $newAccess = $refResp.access
    if ($newAccess) { Write-Host "[+] تم تحديث التوكن (refresh) بنجاح" -ForegroundColor Green }
}
catch { Write-Warning "تعذّر تحديث التوكن عبر refresh: $($_.Exception.Message)" }

Write-Host "[✔] انتهى الاختبار" -ForegroundColor Cyan

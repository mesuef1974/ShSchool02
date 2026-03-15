import os

BASE = r"D:\ShSchool02\backend\apps"

APPS = [
    "core",
    "people",
    "quality",
    "behavior",
    "assessment",
    "attendance",
    "assets",
    "transport",
    "library",
    "hr_school",
    "identity",
    "refdata",
    "comms",
    "health",
    "timetable",
]

SUBFOLDERS = [
    "",
    "models",
    "admin",
]

FILES = {
    "__init__.py": "",
    "apps.py": "",
    "models/__init__.py": "",
    "admin/__init__.py": "",
}

print("Starting structure creation...\n")

for app in APPS:
    app_path = os.path.join(BASE, app)
    print(f"Creating structure for: {app}")

    # إنشاء المجلد الرئيسي للتطبيق
    os.makedirs(app_path, exist_ok=True)

    # إنشاء المجلدات الفرعية
    for sub in SUBFOLDERS:
        os.makedirs(os.path.join(app_path, sub), exist_ok=True)

    # إنشاء الملفات داخل التطبيق
    for file_path, content in FILES.items():
        full_path = os.path.join(app_path, file_path)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

print("\nAll app structures created successfully!")
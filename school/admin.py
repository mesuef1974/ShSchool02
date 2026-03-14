from django.contrib import admin
from . import models

# طھط³ط¬ظٹظ„ طھظ„ظ‚ط§ط¦ظٹ ظ„ط¬ظ…ظٹط¹ ط§ظ„ظ†ظ…ط§ط°ط¬ ط؛ظٹط± ط§ظ„ظ…ط¬ط±ط¯ط©
for name in dir(models):
    obj = getattr(models, name)
    try:
        if hasattr(obj, "_meta") and getattr(obj._meta, "abstract", False) is False:
            admin.site.register(obj)
    except admin.sites.AlreadyRegistered:
        pass


from django.conf import settings

OVERRIDES = getattr(settings, "OVERRIDES", [])

APP_NAMES = [override.split(".")[0] for override in OVERRIDES]


def overrides_name(app):
    """return override file name"""

    file_name = "overrides"

    for override in OVERRIDES:
        if app in override:
            parsed_name = override.split(".")
            if len(parsed_name) > 1:
                file_name = parsed_name[1]
    return file_name


def auto_overrides(app):
    module_name = "%s.%s" % (app, overrides_name(app))
    try:
        __import__(module_name)
    except Exception:
        pass

for app in settings.INSTALLED_APPS:

    if len(APP_NAMES):
        auto_overrides(app)
    elif app in APP_NAMES:
        auto_overrides(app)

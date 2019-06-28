import os


def import_django_settings():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mozio.settings")
    import django; django.setup()  # noqa
    from django.conf import settings  # noqa
    return settings

import os

from django.conf import settings
from django.core.management.templates import TemplateCommand


APPS_DIRECTORY = settings.APPS_DIR
TEMPLATE_BASE_DIR = APPS_DIRECTORY / "core" / "app_template"


class Command(TemplateCommand):
    help = f"Creates a Django app in {APPS_DIRECTORY}"
    missing_args_message = "You must provide an App name."

    def handle(self, **options):
        app_name = options.pop("name")
        _ = options.pop("directory")
        print(f"Creating app {app_name}")
        target = os.path.join(APPS_DIRECTORY, app_name.lower())
        if not os.path.exists(target):
            os.mkdir(target)
        print(f"Installing app on {target}")
        options.update({"template": str(TEMPLATE_BASE_DIR)})
        print("Creating.....")
        super().handle("app", app_name, target, **options)
        print("Successfully installed")
        print(f"**** Add 'ecommerce.{app_name}' to LOCAL_APPS on settings")

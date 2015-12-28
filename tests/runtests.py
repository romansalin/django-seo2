from __future__ import unicode_literals

import os
import sys

# Setup the path (could have been PYTHONPATH)
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


def runtests():
    os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"

    from django.core.wsgi import get_wsgi_application
    get_wsgi_application()

    from django.core.management import call_command
    result = call_command('test', 'userapp')
    sys.exit(result)


if __name__ == "__main__":
    runtests()

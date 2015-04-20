#!/usr/bin/env python
import os
import sys

import django

os.environ["DJANGO_SETTINGS_MODULE"] = "tests.settings"
# Setup the path (could have been PYTHONPATH)
test_dir = os.path.dirname(__file__)
sys.path.insert(0, test_dir)


def runtests():
    django.setup()

    from django.core.management import call_command

    result = call_command('test', 'userapp')
    sys.exit(result)


if __name__ == "__main__":
    runtests()

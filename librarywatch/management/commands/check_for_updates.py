import pip
import xmlrpclib

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

'''
originally based off of:
    https://gist.github.com/3555765

    which was originally based off of:
        http://code.activestate.com/recipes/577708/

'''


class Command(BaseCommand):
    def handle(self, *args, **options):
        pypi = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')

        ignores = getattr(settings, 'LIBRARYWATCH_IGNORE_VERSIONS', {})

        for dist in pip.get_installed_distributions():
            if ignores.get(dist.project_name, '') != '*':  # if it's totally ignored, don't even check.
                available = pypi.package_releases(dist.project_name)
                if not available:
                    # Try to capitalize pkg name
                    available = pypi.package_releases(dist.project_name.capitalize())

                try:
                    if available[0] != dist.version and available[0] != ignores.get(dist.project_name, ''):
                        print '{dist.project_name} ({dist.version} != {available})'.format(dist=dist, available=available[0])

                except IndexError:
                    print('%s is not available on PyPI.' % dist.project_name)

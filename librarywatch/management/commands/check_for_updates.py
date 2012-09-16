import pip
import xmlrpclib

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
        for dist in pip.get_installed_distributions():
            available = pypi.package_releases(dist.project_name)
            if not available:
                # Try to capitalize pkg name
                available = pypi.package_releases(dist.project_name.capitalize())

            try:
                if available[0] != dist.version:
                    print '{dist.project_name} ({dist.version} != {available})'.format(dist=dist, available=available[0])

            except IndexError:
                pass

from django.core.management.base import BaseCommand, CommandError

from srcOptics.scanner.git import Scanner

from srcOptics.models import LoginCredential
import getpass
import requests
import json

#
# The addrepo management command is used to add a repository to the
# database. The user should pass in the URL as the only parameter
#
class Command(BaseCommand):
    help = 'Adds repositories and scans them'

    def add_arguments(self, parser):
        parser.add_argument('-r', '--repo_url', type=str, help='Scan a single repository')

        parser.add_argument('-g',
                            '--github_api',
                            type=str,
                            dest='github_url',
                            help='Scan all repositories in the api endpoint')
        
    def handle(self, *args, **kwargs):

        if len(kwargs) == 0:
            print('No options specified. Please see --help')
            print('  Ex: python manage.py addrepo -r <repo_url>')
            return

        # get the VC credentials and make a LoginCredential before cloning
        username = input('Username: ')
        password = getpass.getpass('Password: ')
        cred = LoginCredential.objects.create(username=username, password=password)

        if kwargs['repo_url']:
            # Scan the repository, passing in the URL and LoginCredential
            Scanner.scan_repo(kwargs['repo_url'], None, cred)


        # Grab a list of repository urls (html_url) from a github
        # API endpoint. The api returns a JSON string, which we can
        # iterate through to get url lists to add.
        #
        # You can use this command with any api point that has
        # a list of 'html_url' entries.
        #
        # Get repositories for a user: https://api.github.com/users/name/repos
        if kwargs['github_url']:
            # GET json data for the api url
            api = requests.get(kwargs['github_url'], auth=(username, password))
            # array of objects for each repo
            data = json.loads(api.text)

            for entry in data:
                Scanner.scan_repo(entry['html_url'], entry['name'], cred)

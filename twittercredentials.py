"""
Twitter Credentials
  Dumps user credential information for user in config file.

Usage:
  twittercredentials
  twittercredentials  (-h | --help | -v | --version)

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
import json
from docopt import docopt
from twitterframework import getAPI

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Twitter Credentials 1.0')

api = getAPI()

credentials_json = api.VerifyCredentials()
credentials = json.loads(str(credentials_json))

for key, value in credentials.items():
    print(key, ':', value)

"""
Twitter Credentials
  Validates the credentials defined in the config file.

Usage:
  twitterconnection  <file>
  twitterconnection  <file> --details
  twitterconnection  (-h | --help | -v | --version)

Options:
  -d --details  Show credential details.
  -h --help     Show this screen.
  -v --version  Show version.
"""
import json
from docopt import docopt
from twitterframework import TwitterAPI

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Twitter Connection 1.0')

twitter_api = TwitterAPI(arguments['<file>'])

try:
    credentials_json = twitter_api.VerifyCredentials()
    if arguments['--details']:
        credentials = json.loads(str(credentials_json))
        for key, value in credentials.items():
            print(key, ':', value)
    else:
        print('pass')
except:
    print('fail')

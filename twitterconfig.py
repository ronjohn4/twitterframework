# Ron Johnson
# 12/6/2016

"""
Twitter Config - creates or updates the specified twitter config file with authentication information.  This
config file is used by other commands to access Twitter.

Usage:
  twitterconfig  <file>  --consumer_key <newConsumerKey>
  twitterconfig  <file>  --consumer_secret <newConsumerSecret>
  twitterconfig  <file>  --access_token_key <newAccessTokenKey>
  twitterconfig  <file>  --access_token_secret <newAccessTokenSecret>
  twitterconfig  <file>  --show
  twitterconfig  [--help | -h | --version | -v]

Options:
  --show         Show current configuration.
  -h, --help     Show this screen.
  -v, --version  Show version.
"""

from docopt import docopt
from twitterframework import TwitterAPI

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Twitter Config 1.0')

config_file = arguments['<file>']
twitter_api = TwitterAPI(config_file)

if arguments['--show']:
    print('Twitter Config')
    print('  consumer_key:', twitter_api.consumer_key)
    print('  consumer_secret:', twitter_api.consumer_secret)
    print('  access_token_key:', twitter_api.access_token_key)
    print('  access_token_secret:', twitter_api.access_token_secret)

if arguments['--consumer_key']:
    twitter_api.consumer_key = arguments['<newConsumerKey>']

if arguments['--consumer_secret']:
    twitter_api.consumer_secret = arguments['<newConsumerSecret>']

if arguments['--access_token_key']:
    twitter_api.access_token_key = arguments['<newAccessTokenKey>']

if arguments['--access_token_secret']:
    twitter_api.access_token_secret = arguments['<newAccessTokenSecret>']

twitter_api.SaveConfig()

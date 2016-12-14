"""
Twitter Stream - writes basic tweet data our to the console in CSV format.

Usage:
  twitterstream  <file> <TwitterKeyword> ...
  twitterstream  (-h | --help | -v | --version)

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from datetime import datetime
from docopt import docopt
from twitterframework import TwitterAPI
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment
import win_unicode_console as win_unicode_console


if __name__ == '__main__':
    arguments = docopt(__doc__, version='Twitter Stream DB 1.0')


twitter_fw = TwitterAPI(arguments['<file>'])
twitter_api = twitter_fw.getAPI()

keylist = [key for key in arguments['<TwitterKeyword>']]
rows = []
win_unicode_console.enable()    # allows printing unicode to windows console

for tweet in twitter_api.GetStreamFilter(follow=None, track=keylist, locations=None, delimited=None, stall_warnings=None):
    t_lang = tweet['lang']
    t_text = tweet['text']

    vs = vaderSentiment(t_text)
    for i, searchtext in enumerate(keylist):
        if searchtext in t_text:
            print("'{0}','{1}','{2}','{3}','{4}','{5}'".format(
                str(datetime.now()),
                str(t_text),
                searchtext,
                str(t_lang),
                vs['pos'],
                vs['neg']
            ))

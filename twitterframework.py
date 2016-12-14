# Ron Johnson
# 12/14/2016
import json
import twitter


class TwitterAPI(object):
    """Represents a Twitter connection.

     Returns an instance of the Twitter API using the contents of the given config file.  A config file can be created
     using the TwitterConfig command.

     Public attributes:
     - config_file:
     - consumer_key:
     - consumer_secret:
     - access_token_key:
     - access_token_secret:
     """
    config_file = ''
    consumer_key = ''
    consumer_secret = ''
    access_token_key = ''
    access_token_secret = ''

    def __init__(self, config_file=None):
        if config_file is None:
            pass
        else:
            try:
                with open(config_file, 'r') as f:
                    config = json.load(f)
                f.close()

                self.config_file = config_file
                self.consumer_key = config['consumer_key']
                self.consumer_secret = config['consumer_secret']
                self.access_token_key = config['access_token_key']
                self.access_token_secret = config['access_token_secret']
            except:
                self.config_file = config_file
                self.consumer_key = ''
                self.consumer_secret = ''
                self.access_token_key = ''
                self.access_token_secret = ''

    def getAPI(self):
        try:
            api = twitter.Api(consumer_key=self.consumer_key,
                              consumer_secret=self.consumer_secret,
                              access_token_key=self.access_token_key,
                              access_token_secret=self.access_token_secret)
            return api
        except:
            raise NameError('Twitter authentication failed')

    def SaveConfig(self, config_file=None):
        """SaveConfg - Save the currently defined config information.  Use the current config file is defined or pass
        in a new file name. """
        if config_file is not None:
            self.config_file = config_file
        if self.config_file == '':
            raise Exception('No config file name defined')

        c = {'consumer_key': self.consumer_key,
             'consumer_secret': self.consumer_secret,
             'access_token_key': self.access_token_key,
             'access_token_secret': self.access_token_secret}

        with open(self.config_file, 'w') as f:
            json.dump(c, f)
        f.close()

    def __repr__(self):
        return 'TwitterAPI(file=%s, consumer_key=%s, Consumer_secret=%s, access_token_key=%s, access_token_secret=%s' % \
               (self.config_file, self.consumer_key, self.consumer_secret, self.access_token_key, self.access_token_secret)
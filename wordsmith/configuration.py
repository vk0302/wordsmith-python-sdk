"""
wordsmith.configuration
~~~~~~~~~~~~~~~~~~~~~~~

This module implements the Wordsmith configuration object.
"""


DEFAULT_VERSION = '1'
DEFAULT_URL = 'https://api.automatedinsights.com/v' + DEFAULT_VERSION
DEFAULT_USER_AGENT = 'PythonSDK'


class Configuration(object):
    """
        Constructs a :class:`Wordsmith <Configuration>` object.

        :param api_key: API key from Wordsmith.
        :param base_url: (optional) String representing the base URL for the
                         Wordsmith API per documentation at
                         http://wordsmith.readme.io/v1/docs
        :param user_agent: (optional) String representing the user agent that
                           should be sent with each API request
        """

    def __init__(self, api_key, **kwargs):
        self.api_key = api_key
        self.base_url = kwargs['base_url'] if 'base_url' in kwargs\
            else self.DEFAULT_URL
        self.user_agent = kwargs['user_agent'] if 'user_agent' in kwargs\
            else self.DEFAULT_USER_AGENT
        self.version = kwargs['version'] if 'version' in kwargs\
            else self.DEFAULT_VERSION

    def get_headers(self):
        """
        Format user agent and auth values as a dictionary for use in GET/POST
        requests to the API
        """
        return {
            'User-Agent': self.user_agent,
            'Authorization': 'Bearer ' + self.api_key
        }

"""
:mod:`irianas_client` -- Is that initiates requests. Wait,
processes and server receives requests.
"""

from irianas_client import metadata


__version__ = metadata.version
__author__ = metadata.authors[0]
__license__ = metadata.license
__copyright__ = metadata.copyright


class ConditionTest(object):
    condition_test = "'VIRTUAL_ENV' in os.environ or TRAVIS' in os.environ"

    def __init__(self):
        super(ConditionTest, self).__init__()

from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres, DEBUG, ERROR

from dropbox.client import DropboxClient
# from dropbox.rest import ErrorResponse


class PydropboxFDW(ForeignDataWrapper):

    _client = None

    def __init__(self, options, columns):
        super(PydropboxFDW, self).__init__(options, columns)

        if 'token' not in options:
            log_to_postgres('access token is not specified', ERROR)

        try:
            self._client = DropboxClient(options['token'])
        except Exception as e:
            log_to_postgres('could not connect to dropbox: %s' % str(e), ERROR)

    def execute(self, quals, columns):
        log_to_postgres('exec quals: %s' % quals, DEBUG)
        log_to_postgres('exec columns: %s' % columns, DEBUG)

        path = '/'
        resp = {}
        try:
            resp = self._client.metadata(path)
        except Exception as e:
            log_to_postgres(
                'could not get metadata for path "%s": %s' % (path, str(e)),
                ERROR)

        for item in resp.get('contents', []):
            yield item

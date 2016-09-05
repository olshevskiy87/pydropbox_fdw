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

        self._path = options.get('path', '/')

        self._metadata_params = {}

        if 'file_limit' in options:
            self._metadata_params['file_limit'] = int(options['file_limit'])

        if 'include_deleted' in options:
            self._metadata_params['include_deleted'] = bool(options['include_deleted'])

        try:
            self._client = DropboxClient(options['token'])
        except Exception as e:
            log_to_postgres('could not connect to dropbox: %s' % str(e), ERROR)

    def execute(self, quals, columns):
        log_to_postgres('exec quals: %s' % quals, DEBUG)
        log_to_postgres('exec columns: %s' % columns, DEBUG)

        resp = {}
        try:
            resp = self._client.metadata(self._path, **self._metadata_params)
        except Exception as e:
            log_to_postgres(
                'could not get metadata for path "%s": %s' % (self._path, str(e)),
                ERROR)

        for item in resp.get('contents', []):
            yield item

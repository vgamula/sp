import json

from .exceptions import WebpackException


class WebpackLoader:
    name = None
    config = None
    stats_data = None

    def __init__(self, name, config):
        self.name = name
        self.config = config

    def load_assets(self):
        if self.config['CACHE'] and self.stats_data:
            return self.stats_data
        with open(self.config['STATS_FILE']) as f:
            self.stats_data = json.load(f)
        return self.stats_data

    def _get_asset_field(self, entry_name, field):
        data = self.load_assets()
        if data['status'] != 'done':
            raise WebpackException(data['message'])
        for chunk in data['chunks'][entry_name]:
            if not chunk['name'].endswith('.map'):
                return chunk[field]
            return chunk['name']
        raise WebpackException('Unhandled error')

    def get_asset_name(self, entry_name):
        return self._get_asset_field(entry_name, 'name')

    def get_asset_public_path(self, entry_name):
        return self._get_asset_field(entry_name, 'publicPath')

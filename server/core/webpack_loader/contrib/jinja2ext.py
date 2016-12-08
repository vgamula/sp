import jinja2.ext

from ..utils import get_loader


def get_bundle(entry_name, bundle_name, config, load_file, static_path='/static/dist/'):
    loader = get_loader(bundle_name, config)
    if load_file:
        asset_name = loader.get_asset_name(entry_name)
        name = '{}{}'.format(static_path, asset_name)
    else:
        name = loader.get_asset_public_path(entry_name)
    return '<script src="{}"></script>'.format(name)


class WebpackExtension(jinja2.ext.Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.globals['get_bundle'] = lambda *a, **k: get_bundle(*a, **k)

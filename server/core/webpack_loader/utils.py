from .loader import WebpackLoader

loaders = {}


def get_loader(name, config) -> WebpackLoader:
    if name not in loaders:
        loaders[name] = WebpackLoader(name, config[name])
    return loaders[name]

import yaml


def load_config(filename):
    with open(filename, 'rt') as f:
        data = yaml.load(f)
    return data

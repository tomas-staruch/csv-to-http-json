import yaml


class Config:
    def __init__(self, raw):
        self.server = ServerConfig(raw['server'])


class ServerConfig:
    def __init__(self, raw):
        self.url = raw['url']
        self.api_key = raw['api_key']


def load(file_name):
    """
    Parse YAML configuration file and produce the corresponding object.
    """

    with open(file_name, "r") as f:
        return Config(yaml.safe_load(f))

from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read("config.cfg")
if API_KEY := config_parser.get("chain", "API_KEY"):
    pass
else:
    raise ValueError(f"API_KEY not set in {config_parser.__repr__()}")

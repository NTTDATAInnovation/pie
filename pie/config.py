from configparser import ConfigParser

config_parser = ConfigParser()
config_parser.read("config.cfg")
if not config_parser.get("chain", "OPENAI_API_KEY"):
    raise ValueError("API_KEY not set in config.cfg")


API_KEY = config_parser.get("chain", "OPENAI_API_KEY")

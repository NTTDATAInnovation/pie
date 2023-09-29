from configparser import ConfigParser

cfg = ConfigParser()
cfg.read("config.cfg")

AZURE_OPENAI_CREDENTIALS = {
    "openai_api_key": cfg.get("OPENAI", "API_KEY"),
    "openai_api_base": cfg.get("OPENAI", "API_BASE"),
    "openai_api_type": "azure",
    "openai_api_version": "2023-05-15",
    "model": cfg.get("OPENAI", "MODEL"),
    "deployment_name": cfg.get("OPENAI", "DEPLOYMENT_NAME"),
    # "openai_organization": cfg.get("OPENAI","ORGANIZATION"),
    # "openai_proxy": cfg.get("OPENAI","PROXY"),
}

import configparser
from pathlib import Path


class ConfigReader:
    """
    Utility class to read configuration settings from config.ini
    """
    _config = None

    @classmethod
    def _load_config(cls):
        if cls._config is None:
            cls._config = configparser.ConfigParser()
            config_path = Path(__file__).resolve().parent.parent / "config" / "config.ini"
            if not config_path.exists():
                raise FileNotFoundError(f"Configuration file not found at: {config_path}")
            cls._config.read(config_path)

    @classmethod
    def get_value(cls, section: str, key: str, fallback=None):
        cls._load_config()
        return cls._config.get(section, key, fallback=fallback)

    @classmethod
    def get_app_url(cls) -> str:
        return cls.get_value("common info", "app_url", fallback="https://tutorialsninja.com/demo/")

    @classmethod
    def get_browser(cls) -> str:
        return cls.get_value("common info", "browser", fallback="chrome").lower()

    @classmethod
    def is_headless(cls) -> bool:
        cls._load_config()
        return cls._config.getboolean("common info", "headless", fallback=True)

    @classmethod
    def get_implicit_wait(cls) -> int:
        cls._load_config()
        return cls._config.getint("common info", "implicit_wait", fallback=10)

    @classmethod
    def get_explicit_wait(cls) -> int:
        cls._load_config()
        return cls._config.getint("common info", "explicit_wait", fallback=15)

    @classmethod
    def get_credential(cls, key: str) -> str:
        return cls.get_value("credentials", key, fallback="")

    @classmethod
    def get_path(cls, key: str) -> str:
        return cls.get_value("paths", key, fallback="")

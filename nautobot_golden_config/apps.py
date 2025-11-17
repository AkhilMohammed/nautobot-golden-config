from nautobot.extras.plugins import PluginConfig

__version__ = "1.0.0"

class NautobotGoldenConfig(PluginConfig):
    __module__ = "nautobot_golden_config"  # Force root package module
    name = "nautobot_golden_config"
    verbose_name = "nautobot_golden_config"
    description = "Custom dashboard for device and KPI health."
    author = "Akhil"
    author_email = "shaikMohammed.AkhilTaj@gmail.com"
    required_settings = []
    default_settings = {}
    min_version = "1.0.0"
    max_version = "3.0.0"
    caching_config = {}

    urls = None  # disable URLs import

    def ready(self):
        super().ready()


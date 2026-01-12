from endstone.plugin import Plugin
from endstone import ColorFormat
from endstone.event import PlayerRespawnEvent, event_handler

class respawnMessage(Plugin):
    api_version = "0.10"
    @event_handler
    def on_player_respawn(self, event: PlayerRespawnEvent):
        player = event.player
        title = self.config.get("title")
        subtitle = self.config.get("subtitle")
        player.send_title(
            title,
            subtitle,
            10,
            60,
            20
        )
    def on_load(self) -> None:
        self.save_default_config()
        self.logger.info("Loaded")
    def on_enable(self) -> None:
        self.save_config()
        self.register_events(self)
        self.logger.info(f"{ColorFormat.GREEN}Enabled")

    def on_disable(self) -> None:
        self.logger.info(f"{ColorFormat.RED}Disabled")
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class MCPSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Environment variables: MCP_HOST, MCP_PORT, MCP_LOG_LEVEL
    host: str = Field(default="127.0.0.1", description="MCP server host")
    port: int = Field(default=8000, description="MCP server port")
    log_level: str = Field(default="INFO", description="Logging level")


class DiscordSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Environment variables: DISCORD_MAX_SHARDS, DISCORD_SESSION_TIMEOUT, etc.
    max_shards: int = Field(default=1, description="Maximum number of shards")
    discord_session_timeout: int = Field(
        default=300, description="Session timeout in seconds"
    )
    reconnect_attempts: int = Field(
        default=5, description="Number of reconnection attempts"
    )
    reconnect_delay: int = Field(
        default=1, description="Delay between reconnection attempts in seconds"
    )


class EventStreamSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Environment variables: EVENT_STREAM_BUFFER_SIZE, EVENT_STREAM_TIMEOUT
    buffer_size: int = Field(
        default=100, description="Event stream buffer size"
    )
    timeout: int = Field(
        default=30, description="Event stream timeout in seconds"
    )


class Settings:
    def __init__(self):
        self.mcp = MCPSettings()
        self.discord = DiscordSettings()
        self.event_stream = EventStreamSettings()

settings = Settings()

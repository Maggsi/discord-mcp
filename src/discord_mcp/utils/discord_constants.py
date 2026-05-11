"""Discord permission flag reference for MCP tool schemas.

Used by Field() descriptions to provide AI models with valid permission name examples.
All values are sourced directly from discord.Permissions.VALID_FLAGS (discord.py 2.x).
"""

PERMISSION_FLAGS: dict[str, int] = {
    "create_instant_invite": 1 << 0,        # 1
    "kick_members": 1 << 1,                 # 2
    "ban_members": 1 << 2,                  # 4
    "administrator": 1 << 3,                # 8
    "manage_channels": 1 << 4,              # 16
    "manage_guild": 1 << 5,                 # 32
    "add_reactions": 1 << 6,                # 64
    "view_audit_log": 1 << 7,               # 128
    "priority_speaker": 1 << 8,             # 256
    "stream": 1 << 9,                       # 512
    "read_messages": 1 << 10,               # 1024
    "view_channel": 1 << 10,                # 1024 (alias for read_messages)
    "send_messages": 1 << 11,               # 2048
    "send_tts_messages": 1 << 12,           # 4096
    "manage_messages": 1 << 13,             # 8192
    "embed_links": 1 << 14,                 # 16384
    "attach_files": 1 << 15,                # 32768
    "read_message_history": 1 << 16,        # 65536
    "mention_everyone": 1 << 17,            # 131072
    "external_emojis": 1 << 18,             # 262144
    "use_external_emojis": 1 << 18,         # 262144 (alias for external_emojis)
    "view_guild_insights": 1 << 19,         # 524288
    "connect": 1 << 20,                     # 1048576
    "speak": 1 << 21,                       # 2097152
    "mute_members": 1 << 22,                # 4194304
    "deafen_members": 1 << 23,              # 8388608
    "move_members": 1 << 24,                # 16777216
    "use_voice_activation": 1 << 25,        # 33554432
    "change_nickname": 1 << 26,             # 67108864
    "manage_nicknames": 1 << 27,            # 134217728
    "manage_roles": 1 << 28,                # 268435456
    "manage_permissions": 1 << 28,          # 268435456 (alias for manage_roles)
    "manage_webhooks": 1 << 29,             # 536870912
    "manage_expressions": 1 << 30,          # 1073741824
    "manage_emojis": 1 << 30,               # 1073741824 (alias for manage_expressions)
    "manage_emojis_and_stickers": 1 << 30,  # 1073741824 (alias for manage_expressions)
    "use_application_commands": 1 << 31,    # 2147483648
    "request_to_speak": 1 << 32,            # 4294967296
    "manage_events": 1 << 33,               # 8589934592
    "manage_threads": 1 << 34,              # 17179869184
    "create_public_threads": 1 << 35,       # 34359738368
    "create_private_threads": 1 << 36,      # 68719476736
    "external_stickers": 1 << 37,           # 137438953472
    "use_external_stickers": 1 << 37,       # 137438953472 (alias for external_stickers)
    "send_messages_in_threads": 1 << 38,    # 274877906944
    "use_embedded_activities": 1 << 39,     # 549755813888
    "moderate_members": 1 << 40,            # 1099511627776
    "use_soundboard": 1 << 42,              # 4398046511104
    "create_expressions": 1 << 43,          # 8796093022208
    "use_external_sounds": 1 << 45,         # 35184372088832
    "send_voice_messages": 1 << 46,         # 70368744177664
}


def get_permission_names() -> list[str]:
    """Return a sorted list of all Discord permission flag names.

    Includes both primary flags and aliases as they appear in discord.Permissions.VALID_FLAGS.
    Useful for generating Field() examples in MCP tool schemas.

    Returns:
        List of permission flag name strings, sorted alphabetically.
    """
    return sorted(PERMISSION_FLAGS.keys())


def parse_permission_names_to_ints(perm_string: str) -> int:
    """Convert a comma-separated string of permission names to an integer bitmask."""
    value = 0
    for name in perm_string.split(","):
        name = name.strip()
        if name in PERMISSION_FLAGS:
            value |= PERMISSION_FLAGS[name]
        else:
            raise ValueError(f"Unknown permission flag: {name}")
    return value

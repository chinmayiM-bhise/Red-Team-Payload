import platform
import os


def execute_command(command):

    allowed_commands = [
        "whoami",
        "hostname",
        "systeminfo"
    ]

    if command not in allowed_commands:
        return "Command blocked in simulation mode"

    if command == "whoami":
        return os.getlogin()

    if command == "hostname":
        return platform.node()

    if command == "systeminfo":
        return platform.platform()
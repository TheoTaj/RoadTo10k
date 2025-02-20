import discord_notify as dn
import requests


URL = "https://discord.com/api/webhooks/1339891942691176548/nM0defw-KnPYssBlWBXyPgOWv0ZL7jm7THr69zfD4jOWhLlFe2G8cjn9mIKf1mo8lvWM"


def discord(message):
    notifier = dn.Notifier(URL)
    notifier.send(message, print_message = False)


def send_file_to_discord(file_path, message="Details :"):
    with open(file_path, "rb") as file:
        data = {
            "content": message
        }
        files = {
            "file": file
        }
        response = requests.post(URL, data=data, files=files)


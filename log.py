import discord_notify as dn

URL = "https://discord.com/api/webhooks/1339891942691176548/nM0defw-KnPYssBlWBXyPgOWv0ZL7jm7THr69zfD4jOWhLlFe2G8cjn9mIKf1mo8lvWM"


def discord(message):
    notifier = dn.Notifier(URL)
    notifier.send(message, print_message = False)
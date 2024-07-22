@echo off
taskkill /F /IM python.exe /T
taskkill /F /IM daphne.exe /T
taskkill /F /IM cmd.exe /T

echo All services stopped. Press any key to exit this window.
pause > nul
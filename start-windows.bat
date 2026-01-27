@echo off

echo Installing modules...
echo.
python3 -m pip install -r requirements.txt
python3 -m pip install "discord.py==2.6.3"
echo.
echo Done! Starting program...
echo.
start gui.pyw
@echo off

echo Installing modules...
echo.
python3 -m pip uninstall discord.py
python3 -m pip install -r requirements.txt
echo.
echo Done! Starting program...
echo.
start gui.pyw
@echo off

title blang Setup
mode con COLS=55 LINES=30
cd %userprofile%\Desktop

echo Installing blang. This might take at most 5 minutes.
powershell "iwr https://www.python.org/ftp/python/3.8.0/python-3.8.0-embed-win32.zip -OutFile runtime.zip" > nul
powershell "expand-archive runtime.zip" > nul
del runtime.zip
cd runtime
powershell "iwr https://raw.githubusercontent.com/Ganesha2282882/blang/main/app.py -OutFile blang.py" > nul
cd ..
ren runtime blang
move blang C:\ > nul
echo Installation complete.
echo You just have to run blang.py
echo with 'python' in front of it like this:
echo python blang.py INSERT BLANG SCRIPT HERE
echo Also, it's installed at 'C:\blang'.
echo Press any key to exit this installer.
pause > nul

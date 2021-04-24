@echo off

mode con COLS=55 LINES=30
title blang Uninstaller

echo Uninstalling blang.
rd c:\blang /s /q

echo Sad to see you go! Maybe next time you would try out blang?
echo Anyway, it's completely uninstalled.
echo blang scripts in there are moved to a
echo folder on your desktop 'blang Scripts'.
echo Press any key to exit this uninstaller.
pause > nul

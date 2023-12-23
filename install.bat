@echo off

rem Read each line from the text file and run 'pip install' for each entry
for /f "delims=" %%i in (requirements.txt) do pip install %%i
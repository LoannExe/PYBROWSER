@echo off
title PyBrowser Requirements Installer
color 0A

:MENU
cls
echo ============================================
echo      PYBROWSER REQUIREMENTS INSTALLER
echo ============================================
echo.
echo 1. Install requirements
echo 2. Download Python
echo 3. Exit
echo 4. Help
echo.
set /p choice=Enter your choice (1-4) : 

if "%choice%"=="1" goto INSTALL_REQUIREMENTS
if "%choice%"=="2" goto DOWNLOAD_PYTHON
if "%choice%"=="3" goto EXIT
if "%choice%"=="4" goto HELP
echo [!] Invalid choice. Please select a valid option.
goto MENU

:INSTALL_REQUIREMENTS
cls
echo [*] Installing Python packages...
echo.

REM Check if pip is available
python -m pip --version >nul 2>&1
if errorlevel 1 (
    echo [!] pip is not installed or Python is not in the PATH.
    echo     Please install Python or add it to your PATH.
    pause
    goto MENU
)

REM Replace this line with your own modules
python -m pip install PyQt5

echo.
echo [!] Download Complete.
pause
goto MENU

:DOWNLOAD_PYTHON
start https://www.python.org/downloads/
goto MENU

:EXIT
echo.
echo Enjoy your experience with PyBrowser!
timeout /t 2 >nul
exit

:HELP
cls
echo ============================================
echo                HELP MENU
echo ============================================
echo.
echo The required Python package is PyQt5.
echo You can manually install it using the command:
echo python -m pip install PyQt5
echo.
echo If you need to download Python, select option 2.
echo If you encounter any issues, please contact "notloann" on Discord!
echo.
echo Press any key to return to the main menu...
pause >nul
goto MENU
REM End of INSTALL_REQUIREMENTS.bat
REM This script installs the required Python packages for PyBrowser.
REM It also provides options to download Python and display help information.
@echo off
setlocal enabledelayedexpansion

:: Solicitar nombre del entorno
set /p ENABLE_CUDA=¿Deseas soporte CUDA? (s/n):

:: Preguntar por soporte CUDA
if /I "!ENABLE_CUDA!"=="s" (
    set FORCE_CMAKE=1
    set CMAKE_ARGS=-DLLAMA_CUDA=on
    echo "Soporte CUDA habilitado."
) else (
    echo "Soporte CUDA desactivado."
)

:: Crear y activar entorno virtual
echo Creando entorno virtual...
python -m venv venv
if errorlevel 1 (
    echo Error al crear el entorno virtual.
    exit /b 1
)

call "venv\Scripts\activate.bat"
if errorlevel 1 (
    echo Error al activar el entorno virtual.
    exit /b 1
)

:: Instalar herramientas básicas
echo Instalando pip, cmake y wheel...
::python.exe -m pip install --upgrade pip
pip install --upgrade pip --no-cache-dir --force-reinstall cmake wheel scikit-build-core ninja


:: Instalar llama-cpp-python
pip install llama-cpp-python --no-cache-dir --force-reinstall --verbose

:: Mostrar resumen
echo ========================================
echo Instalación completada.
if /I "%ENABLE_CUDA%"=="s" (
    echo CUDA: SÍ
) else (
    echo CUDA: NO
)

echo ===================================xD===
echo.

pause

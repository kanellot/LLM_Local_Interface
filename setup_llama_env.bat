@echo off
setlocal enabledelayedexpansion

:: Solicitar nombre del entorno
set /p ENV_NAME=Nombre del entorno virtual (ej: venv):

:: Preguntar por soporte CUDA
set /p ENABLE_CUDA=¿Deseas soporte CUDA? (s/n):
if /I "%ENABLE_CUDA%"=="s" (
    set "CMAKE_CUDA=--config-settings=cmake.define.LLAMA_CUDA=on"
    echo Soporte CUDA habilitado.
) else (
    set "CMAKE_CUDA="
    echo Soporte CUDA desactivado.
)

:: Preguntar por modo debug
set /p ENABLE_DEBUG=¿Deseas modo debug? (s/n):
if /I "%ENABLE_DEBUG%"=="s" (
    set "CMAKE_DEBUG="
    echo Modo debug habilitado (salida por consola activa).
) else (
    set "CMAKE_DEBUG=--config-settings=cmake.define.LLAMA_LOG_DISABLE=on"
    echo Modo debug desactivado (no se mostrará salida de trazas).
)

:: Crear y activar entorno virtual
python -m venv %ENV_NAME%
call %ENV_NAME%\Scripts\activate

:: Instalar dependencias
pip install --upgrade pip
pip install cmake
pip install wheel

:: Inicializar submódulos por si no están listos
git submodule update --init --recursive

:: Crear requirements.txt si no existe
if not exist requirements.txt (
    echo llama-cpp-python > requirements.txt
)

:: Instalar llama-cpp-python con opciones seleccionadas
pip install -r requirements.txt
pip install . --force-reinstall --no-cache-dir --no-build-isolation %CMAKE_CUDA% %CMAKE_DEBUG%

echo.
echo Instalación completada.
echo Entorno virtual: %ENV_NAME%
if not "%ENABLE_CUDA%"=="s" echo > CUDA: NO
if "%ENABLE_CUDA%"=="s" echo > CUDA: SÍ
if not "%ENABLE_DEBUG%"=="s" echo > DEBUG: NO
if "%ENABLE_DEBUG%"=="s" echo > DEBUG: SÍ

pause

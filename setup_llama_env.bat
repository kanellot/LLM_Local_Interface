@echo off
setlocal enabledelayedexpansion

:: Solicitar nombre del entorno
set /p ENABLE_CUDA=¿Deseas soporte CUDA? (s/n):

:: Preguntar por soporte CUDA
if /I "!ENABLE_CUDA!"=="s" (
    set "CMAKE_CUDA=--config-settings=cmake.define.LLAMA_CUDA=on"
    echo "Soporte CUDA habilitado."
) else (
    set "CMAKE_CUDA="
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
pip install --upgrade pip
pip install cmake wheel
pip install scikit-build-core ninja


:: Inicializar submódulos si es necesario
echo Verificando submódulos de Git...


::
::cmake -B build -DLLAMA_CUDA=ON
::cmake --build build --config Release

:: Instalar llama-cpp-python 
::pip install llama-cpp-python --no-cache-dir --no-build-isolation
set FORCE_CMAKE=1
set CMAKE_ARGS=-DLLAMA_CUDA=on
pip install llama-cpp-python --verbose
pip install llama-cpp-python 
git submodule update --init --recursive

:: Clona llama.cpp si no existe
::if not exist llama.cpp (
::    git clone https://github.com/ggerganov/llama.cpp.git
::)

::cd llama.cpp

:: Compila según respuesta
::if /I "!ENABLE_CUDA!"=="s" (
::    echo Compilando con soporte CUDA...
::    cmake -B build -DLLAMA_CUDA=ON
::    cmake --build build --config Release
::) else (
::    echo Compilando sin soporte CUDA...
::    cmake -B build
::    cmake --build build --config Release
::)



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

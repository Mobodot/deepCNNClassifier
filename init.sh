echo [$(date)]: "START"
export _VERSION_=3.8
echo [$(date)]: "Creating environment with python version: ${_VERSION_}"
conda create --prefix ./env python=${_VERSION_} -y
echo [$(date)]: "Activating environment"
source activate ./env
echo [$(date)]: "Installing the dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"

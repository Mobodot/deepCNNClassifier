import os
import logging
from pathlib import Path


logging.basicConfig(
     level=logging.INFO,
     format="[%(asctime)s: %(levelname)s:] %(message)s"
)


while True:
    project_name = input("Enter project name: ")
    if project_name != "":
        break


logging.info(f"Creating project by name: {project_name}")


LIST_OF_PATHS = [
    ".github/workflows/.gitkeep",
    "configs/config.yaml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    "tests/__init__.py",
    "tests/integration/__init__.py",
    "tests/unit/__init__.py",
    "requirements.txt",
    "requirements_dev.txt",
    "dvc.yaml",
    "params.yaml",
    "setup.cfg",
    "setup.py",
    "tox.ini",
    "pyproject.toml",
    "init.sh",
    "research/trials.ipynb"
]


for filepath in LIST_OF_PATHS:
    filepath = Path(filepath)
    file_dir, file_name = os.path.split(filepath)
    if file_dir != "":
        logging.info(f"Creating directory: {file_dir} for file: {file_name}")
        os.makedirs(name=file_dir, exist_ok=True)
        
    if (not os.path.exists(filepath) or os.path.getsize(filepath) == 0):
        with open(Path(filepath), "w") as f:
            pass # create an empty 
            logging.info(f"Creating an empty file: {file_name} in: {filepath}")
            
    else:
        logging.info(f"File is already present at {filepath}")
    
    
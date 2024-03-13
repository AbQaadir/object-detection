import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


project_name = "signLanguage"

list_of_files = [
    "data/.gitkeep",
    "docs/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/configuration/s3_operations.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py"
    "template/index.html",
    ".dockerignore",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    
]




for filepath in list_of_files:
  filepath = Path(filepath)  # Convert the filepath to a Path object

  # Split the filepath into the directory path and filename
  filedir, filename = os.path.split(filepath)

  # Create the directory if it doesn't exist, ignoring errors if it already exists
  if filedir != "":
    os.makedirs(filedir, exist_ok=True)

  # Check if the file exists and is empty
  if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
    # Create an empty file
    with open(filepath, 'w') as f:
      pass
    logging.info(f"Creating empty file: {filename}")
  else:
    logging.info(f"{filename} is already created")

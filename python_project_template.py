import os

# Define the project structure
project_structure = {
    "project_name": {
        "data": {
            "raw": {},
            "processed": {}
        },
        "notebooks": {
            "exploration": {},
            "analysis": {},
            "reports": {}
        },
        "src": {
            "__init__.py": "",
            "data_processing.py": """import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def clean_data(df):
    # Implement data cleaning steps
    return df
""",
            "visualization.py": "",
            "model.py": ""
        },
        "tests": {
            "test_data_processing.py": """import pytest
from src.data_processing import load_data, clean_data

def test_load_data():
    df = load_data('data/raw/sample.csv')
    assert not df.empty

def test_clean_data():
    df = load_data('data/raw/sample.csv')
    cleaned_df = clean_data(df)
    assert cleaned_df.isna().sum().sum() == 0
""",
            "test_visualization.py": "",
            "test_model.py": ""
        },
        "docs": {
            "project_overview.md": ""
        },
        "environment.yml": """name: project_name
channels:
  - defaults
dependencies:
  - python=3.9
  - jupyterlab
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - scikit-learn
  - pytest
""",
        "requirements.txt": """jupyterlab
numpy
pandas
matplotlib
seaborn
scikit-learn
pytest
""",
        "setup.py": """from setuptools import setup, find_packages

setup(
    name='project_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'seaborn',
        'scikit-learn',
        'pytest',
        'jupyterlab'
    ],
)
""",
        "README.md": """# Project Name

## Overview
A brief description of the project.

## Setup
Instructions to set up the environment:
\`\`\`bash
conda env create -f environment.yml
conda activate project_name
\`\`\`

## Usage
How to run the code or notebooks.
""",
        ".gitignore": """# Ignore Python cache files
__pycache__/
*.pyc

# Ignore data files
data/raw/
data/processed/

# Ignore Jupyter notebook checkpoints
.ipynb_checkpoints/

# Ignore environment files
.env
*.env
"""
    }
}

# Function to create the project structure
def create_project_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_project_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)

# Create the project
project_name = "project_name"
create_project_structure(project_name, project_structure)


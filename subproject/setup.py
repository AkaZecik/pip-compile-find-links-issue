from setuptools import setup
from pathlib import Path
import os.path

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
REQUIREMENTS_PATH = BASE_DIR / "requirements.txt"


with REQUIREMENTS_PATH.open() as f:
    stripped_rq_lines = [line.strip() for line in f.read().splitlines()]

install_requires = [
    line for line in stripped_rq_lines if line and not line.startswith("#")
]


setup(
    name="subproject",
    version="1.0.0",
    description="My subproject",
    install_requires=install_requires,
    python_requires=">=3.8,<3.9",
)


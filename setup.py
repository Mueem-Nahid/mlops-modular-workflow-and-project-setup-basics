from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

# read readme file for long description 
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mlops-modular-workflow-and-project-setup-basics",
    version="0.1.0",
    author="Mueem Nahid",
    author_email="mueem51@gmail.com",
    description="This project is based on mlops modular workflow and project setup basics.",
    long_description=long_description,
    url="https://github.com/Mueem-Nahid/mlops-modular-workflow-and-project-setup-basics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Beta",
        "Intended Audience :: ML Engineers",
        "Programming Language :: Python >= 3.8",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=required,
    extras_require={
        'dev': [
            'pytest>=7.1.1',
            'pytest-cov>=2.12.1',
            'flake8>=3.9.0',
            'black>=22.3.0',
            'isort>=5.10.1',
            'mypy>=0.942',
        ],
    }
)

# to install this setup.py run, pip install -e .
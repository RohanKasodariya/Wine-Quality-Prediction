"""
setup.py is the build script for setuptools, which is the standard tool used for packaging Python projects.

What it does:
-------------
This file defines the metadata and configuration for the WineQualityPrediction package, making it installable 
and distributable. When someone runs `pip install .` in this project directory, setuptools will use this file 
to understand how to install the package and its dependencies.

Why it's needed:
----------------
1. It allows your project to be treated as a Python package.
2. You can install it locally or upload it to PyPI for public/private sharing.
3. It specifies where the source code is (`src/`), and what files and modules should be packaged.
4. It contains metadata such as name, version, author, description, and GitHub URL.
5. Tools like pip, CI/CD pipelines, or Docker use it to install and run your code correctly.

Structure of this setup:
-------------------------
- `name` and `version`: Package identity.
- `author` and `email`: Author metadata.
- `description` and `long_description`: Helpful for documentation on PyPI or GitHub.
- `url` and `project_urls`: Links to your repo and issue tracker.
- `packages=find_packages(where="src")`: Automatically includes all subpackages in the `src/` directory.
- `package_dir={"": "src"}`: Tells setuptools that the source code is in the `src` folder.

By defining this setup.py, the WineQualityPrediction project can be cleanly installed, imported, reused, and distributed.
"""

import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Wine-Quality-Prediction"
AUTHOR_USER_NAME = "RohanKasodariya"
SRC_REPO = "WineQualityPrediction"
AUTHOR_EMAIL = "rohankasodariya30@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author=AUTHOR_USER_NAME,
    description= "A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls= {
      "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
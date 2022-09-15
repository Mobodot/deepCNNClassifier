from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__VERSION__ = "0.0.0"

SRC_REPO = "deepClassifier"
AUTHOR_NAME = "Mobodot"
AUTHOR_EMAIL = "mobosomto@gmail.com"


setup(
    name=SRC_REPO,
    version=__VERSION__,
    author="AUTHOR_NAME",
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{SRC_REPO}/issues"
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
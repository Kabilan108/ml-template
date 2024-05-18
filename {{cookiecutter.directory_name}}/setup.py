from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.short_name}}",
    version="0.0.1",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    description="",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
)

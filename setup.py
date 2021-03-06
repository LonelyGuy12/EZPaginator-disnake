from setuptools import setup, find_packages
from EZPaginator import __version__

setup(
    name="EZPaginator",
    license="MIT",
    version=__version__,
    description="Python wrapper for disnake pagination.",
    author="khk4912",
    author_email="khk49121@gmail.com",
    url="https://github.com/khk4912/EZPaginator",
    packages=find_packages(),
    keywords=["disnake", "paginaion"],
    python_requires=">=3.6",
    install_requires=["disnake"],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)

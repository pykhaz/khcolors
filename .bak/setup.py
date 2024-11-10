from setuptools import setup, find_packages

setup(
    name="khcolors",
    version="0.1.0",
    description="Searching for a CSS colour or a colour in the rich library",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="khaz",
    author_email="pykhaz@o2.pl",
    url="https://github.com/heliotech/khcolors",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "rich",
    ],
    entry_points={
        'console_scripts': [
            'khcolors=khcolors.__main__:main',
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires='>=3.8',
)

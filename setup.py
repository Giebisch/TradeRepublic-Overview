import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="traderep",
    entry_points = {
        "console_scripts": ["traderep = traderep.traderep:main"]
    },
    version="1.0",
    author="Giebisch",
    author_email="rafael@giebisch-mail.de",
    description="Application for parsing positions and \
        displaying their current market value",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Giebisch/TradeRepublic-Overview",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

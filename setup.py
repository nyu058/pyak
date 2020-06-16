import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyak", 
    version="0.0.3",
    author="Nathan Yu",
    author_email="nathan5508@gmail.com",
    description="A Python cli tools to automically press a key after some time interval.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nyu058/pyak",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS",
    ],
    install_requires=['psutil','pyautogui'],
    python_requires='>=3.5',
    entry_points={
        'console_scripts':['pyak=src.pyak:run']
    }
)
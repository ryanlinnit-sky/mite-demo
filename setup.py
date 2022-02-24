import setuptools

setuptools.setup(
    install_requires=[
        "acurl-ng @ git+https://github.com/sky-uk/mite@master#egg=acurl_ng&subdirectory=acurl_ng",
        "acurl @ git+https://github.com/sky-uk/mite@master#egg=acurl&subdirectory=acurl",
        "mite @ git+https://github.com/sky-uk/mite@master#egg=mite",
    ]
)
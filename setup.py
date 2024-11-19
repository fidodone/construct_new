#!/usr/bin/env python
from setuptools import setup
from construct_new.version import version_string

setup(
    name="construct_new",  # Novo nome do módulo
    version=version_string,
    packages=[
        'construct_new',  # Atualizado para o novo nome
        'construct_new.lib',  # Atualizado para o novo nome
    ],
    license="MIT",
    description="A powerful declarative symmetric parser/builder for binary data",
    long_description=open("README.rst").read(),
    platforms=["POSIX", "Windows"],
    url="http://construct.readthedocs.org",
    project_urls={
        "Source": "https://github.com/construct/construct",  # Atualize para o URL do fork
        "Documentation": "https://construct.readthedocs.io/en/latest/",
        "Issues": "https://github.com/construct/construct/issues",  # Atualize para o URL do fork
    },
    author="Arkadiusz Bulski, Tomer Filiba, Corbin Simpson",
    author_email="arek.bulski@gmail.com, tomerfiliba@gmail.com, MostAwesomeDude@gmail.com",
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "extras": [
            "numpy",
            "arrow",
            "ruamel.yaml",
            "cloudpickle",
            "lz4",
            "cryptography",
        ],
    },
    keywords=[
        "construct",
        "construct_new",  # Inclui o novo nome como palavra-chave
        "kaitai",
        "declarative",
        "data structure",
        "struct",
        "binary",
        "symmetric",
        "parser",
        "builder",
        "parsing",
        "building",
        "pack",
        "unpack",
        "packer",
        "unpacker",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Code Generators",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)

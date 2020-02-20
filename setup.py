import setuptools

setuptools.setup(
    name="cli",
    version="0.0.1",
    install_requires=["click"],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    entry_points={"console_scripts": [
        "mycli1 = cli.base:cli",
        "mycli2 = cli.cli:cli",
    ]}
)
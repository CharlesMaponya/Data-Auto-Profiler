from setuptools import setup, find_packages

setup(
    name="autoprofile",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas>=2.2.2",
        "numpy>=1.26.4",
        "plotly>=5.22.0",
        "scipy>=1.13.1"
    ],
    python_requires=">=3.8"
)
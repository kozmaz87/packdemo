
from setuptools import setup

packages = [
    "le_demo",
    "le_demo.scripts"
]

setup(
    name="le-demo",
    version="0.0.1",
    description="Zoltan's Package for his excellent packaging presentation :)",
    install_requires=[],
    license="BSD3",
    packages=packages,
    entry_points={
        "console_scripts": [
            "demo-script = le_demo.scripts.demo_script:main",
        ]
    },
    include_package_data=True
)

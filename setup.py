from setuptools import setup

setup(
    name="flake8_backend_url",
    version="0.1.0",
    description="Flake8 plugin to check for specific URL pattern in settings.BACKEND_BASE_URL",
    py_modules=["flake8_backend_url"],
    install_requires=["flake8 > 3.0.0"],
    entry_points={
        "flake8.extension": [
            "URLP = flake8_backend_url:URLPatternChecker",
        ],
    },
    classifiers=[
        "Framework :: Flake8",
    ],
)
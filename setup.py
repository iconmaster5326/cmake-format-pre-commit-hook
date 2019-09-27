from setuptools import setup


setup(
    name="cmake_format_pre_commit_hook",
    entry_points={
        "console_scripts": [
            "cmake_format_pre_commit_hook=cmake_format_pre_commit_hook:main"
        ]
    },
    packages=["cmake_format_pre_commit_hook"],
    install_requires=["cmake-format", "pyyaml"],
)

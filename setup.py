#
# Author: Joed Lopes da Silva
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

from setuptools import setup


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="uihelper",
    version="0.0.2",
    author="Joed Lopes da Silva",
    author_email="joedlopes@github.com",
    description="The helper for GUI using PySide6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joedlopes/uihelper",
    project_urls={
        "Bug Tracker": "https://github.com/joedlopes/uihelper/issues",
    },
    install_requires=["pyside6", "pydantic", "pyqtgraph", "pyopengl", "numpy"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=[
        "uihelper",
        "uihelper.helpers",
        "uihelper.resources",
        "uihelper.widgets",
        "uihelper.widgets.property_editor_tree",
    ],
    # include non python files
    package_data={
        "uihelper.widgets.property_editor_tree": [
            "uihelper/widgets/property_editor_tree/icons/*.png"
        ],
    },
    include_package_data=True,
    python_requires=">=3.8",
)

"""This module is called after project is created.

From pydanny's cookiecutter-django:
https://github.com/pydanny/cookiecutter-django
And:
https://github.com/wemake-services/wemake-python-package
"""

from os import system
from os.path import curdir, realpath
from shutil import rmtree
from sys import exit
from textwrap import dedent

# Get the root project directory:
PROJECT_DIRECTORY = realpath(curdir)
PROJECT_NAME = "{{ cookiecutter.project_name }}"

# Translations info
OTHER_LANGUAGES_SUPPORT = "{{ cookiecutter.other_languages_support }}"
UKRAINIAN_LANGUAGE_SUPPORT = "{{ cookiecutter.ukrainian_language_support }}"
RUSSIAN_LANGUAGE_SUPPORT = "{{ cookiecutter.russian_language_support }}"

# We need these values to generate correct license:
LICENSE = "{{ cookiecutter.license }}"
ORGANIZATION = "{{ cookiecutter.organization }}"


def generate_license() -> None:
    """Generates license file for the project."""
    license_result = system(  # noqa: S605
        "lice {0} -o {1} -p {2} > {3}/LICENSE".format(
            LICENSE.lower(),
            ORGANIZATION,
            PROJECT_NAME,
            PROJECT_DIRECTORY,
        ),
    )
    if license_result:  # it means that return code is not 0, print exception
        print(license_result)  # noqa: WPS421
        exit(1)


def handle_translations() -> None:
    """Delete specific or all translation files, depends on configuration."""
    if not OTHER_LANGUAGES_SUPPORT == "y":
        rmtree(f"{PROJECT_DIRECTORY}/locales")
        rmtree(f"{PROJECT_DIRECTORY}/docs/locale")
        return

    if not UKRAINIAN_LANGUAGE_SUPPORT == "y":
        rmtree(f"{PROJECT_DIRECTORY}/locales/uk")
        rmtree(f"{PROJECT_DIRECTORY}/docs/locale/uk_UA")

    if not RUSSIAN_LANGUAGE_SUPPORT == "y":
        rmtree(f"{PROJECT_DIRECTORY}/locales/ru")
        rmtree(f"{PROJECT_DIRECTORY}/docs/locale/ru")


def print_futher_instuctions() -> None:
    """Shows user what to do next after project creation."""
    message = """
    Your project {0} is created.
    Now you can start working on it:
        cd {0}
    """
    print(dedent(message.format(PROJECT_NAME)))  # noqa: WPS421


generate_license()
handle_translations()
print_futher_instuctions()

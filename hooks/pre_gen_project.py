from re import match
from sys import exit

MODULE_REGEX = r"^[a-z][a-z0-9\-]+[a-z0-9]$"
MODULE_NAME = "{{ cookiecutter.project_name }}"

OTHER_LANGUAGES_SUPPORT = "{{ cookiecutter.other_languages_support }}"
UKRAINIAN_LANGUAGE_SUPPORT = "{{ cookiecutter.ukrainian_language_support }}"
RUSSIAN_LANGUAGE_SUPPORT = "{{ cookiecutter.russian_language_support }}"


def validate_bool_values() -> None:
    """This validator is used to ensure that all bool values is valid.

    Raises:
        ValueError: When one of bool values is not ``y`` or ``n``.
    """
    for bool_value in [OTHER_LANGUAGES_SUPPORT, UKRAINIAN_LANGUAGE_SUPPORT, RUSSIAN_LANGUAGE_SUPPORT]:
        if bool_value not in ["y", "n"]:
            raise ValueError("ERROR: The value of {0} is not a `y` or `n`.".format(bool_value))


def validate_project_name() -> None:
    """This validator is used to ensure that `project_name` is valid.

    Valid inputs starts with the lowercase letter.
    Followed by any lowercase letters, numbers or hyphens.
    Ends with a lowercase letter or number.

    Valid example: `school-project3`.

    Raises:
        When project name not valid.
    """
    if not match(MODULE_REGEX, MODULE_NAME):
        # Validates project"s module name:
        message = [
            "ERROR: The project slug {0} is not a valid Python module name.",
            "Start with a lowercase letter.",
            "Followed by any lowercase letters, numbers or hyphens (-).",
            "End with a lowercase letter or number.",
        ]
        if "_" in MODULE_NAME:
            message.append("Do not use underscores (_) in your project name.")
        raise ValueError(" ".join(message).format(MODULE_NAME))


try:
    validate_bool_values()
    validate_project_name()
except ValueError as ex:
    print(ex)
    exit(1)

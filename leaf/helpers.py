"""Django leaf helpers."""
import re


def camelcase_to_underscore(name):
    """Convert camel case string to underscores.

    Reference:
        * http://stackoverflow.com/a/1176023/1527753

    :param str name: The CamelCase string to convert
    :returns: A string of the CamelCase with underscores (CamelCase -> camel_case)

    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

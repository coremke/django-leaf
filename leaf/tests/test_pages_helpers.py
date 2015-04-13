import pytest


@pytest.mark.parametrize("camel,expected", (
    ("TestingThis", "testing_this"),
    ("TestingThisAgain2", "testing_this_again2"),
    ("Testingthis", "testingthis"),
    ("testing_this", "testing_this"),
))
def test_camelcase_to_underscore(camel, expected):
    from leaf.helpers import camelcase_to_underscore

    assert camelcase_to_underscore(camel) == expected

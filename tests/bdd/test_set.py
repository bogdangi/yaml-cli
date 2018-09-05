# coding=utf-8
"""Set feature tests."""
from main import yaml
import sys

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

sys.path.append('../..')


@scenario('features/set.feature', 'Set a value in simple yaml file')
def test_set_a_value_in_simple_yaml_file():
    """Set a value in simple yaml file."""


@given('I change in the yaml file with <content_before> a <value>')
def output(content_before, value):
    """I change in the yaml file with <content_before> a <value>."""
    input = '\n'.join(content_before.split('\\n'))
    return yaml(input, value)


@then('I should see the file with <content_after>')
def i_should_see_the_changes_in_the_file(
    content_after,
    output
):
    """I should see the changes in the file."""
    assert '\n'.join(content_after.split('\\n')) == output

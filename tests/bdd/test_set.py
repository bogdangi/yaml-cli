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


@given('there is a yaml file with <content_before>')
def input(content_before):
    """there is a yaml file."""
    return '\n'.join(content_before.split('\\n'))


@when('I change the yaml file with <value>')
@given('output')
def output(input, value):
    """I change the yaml file."""
    return yaml(input, value)


@then('I should see the file with <content_after>')
def i_should_see_the_changes_in_the_file(
    content_after,
    output
):
    """I should see the changes in the file."""
    assert output == '\n'.join(content_after.split('\\n'))

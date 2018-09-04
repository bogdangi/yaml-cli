Feature: Set
    Set a value in yaml file

Scenario: Set a value in simple yaml file
    Given there is a yaml file with <content_before>
    When I change the yaml file with <value>
    Then I should see the file with <content_after>

    Examples:
        | content_before     | value         | content_after      |
        | user:\n  name: bob | user.name=ted | user:\n  name: ted\n |

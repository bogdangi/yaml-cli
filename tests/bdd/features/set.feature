Feature: Set
    Set a value in yaml file

Scenario: Set a value in simple yaml file
    Given there is a yaml file with <content_before>
    When I change the yaml file with <value>
    Then I should see the file with <content_after>

    Examples:
        | content_before     | value         | content_after        |
        | name: bob\n        | name=ted      | name: ted\n          |
        | user:\n  name: bob | user.name=ted | user:\n  name: ted\n |
        | a:\n- b\n- c\n     | a.0=a         | a:\n- a\n- c\n       |
        | a:\n- b\n- c\n     | a.0.a=b       | a:\n- a: b\n- c\n    |
        | a:\n- b\n          | a.1.c=b       | a:\n- b\n- c: b\n    |

Feature: Set
    Set a value in yaml file

Scenario: Set a value in simple yaml file
    Given I change in the yaml file with <content_before> a <value>
    Then I should see the file with <content_after>

    Examples:
        | content_before     | value         | content_after         |
        | name: bob\n        | name=ted      | name: ted\n           |
        | user:\n  name: bob | user.name=ted | user:\n  name: ted\n  |
        | a:\n- b\n- c\n     | a.0=a         | a:\n- a\n- c\n        |
        | a:\n- b\n- c\n     | a.0.a=b       | a:\n- a: b\n- c\n     |
        | a: b\n             | a.b.c=d       | a:\n  b:\n    c: d\n  |
        | a:\n- b\n          | a.1.c=b       | a:\n- b\n- c: b\n     |
        | x: t\n             | a.0.c=b       | x: t\na:\n- c: b\n    |
        | a:\n- b: c\n       | a.0.d=e       | a:\n- b: c\n  d: e\n  |
        | \n                 | a.0.d=e       | a:\n- d: e\n          |
        | # comments\na: b\n | a=c           | # comments\na: c\n    |
        | a:\n- b\n          | a.[]=c        | a:\n- b\n- c\n        |

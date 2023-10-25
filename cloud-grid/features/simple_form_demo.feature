Feature: Simple Form Demo

  Scenario: Entering a message
    Given the user is on the Simple Form Demo page
    When the user enters the message "My pytest-bdd message" in the input field
    And clicks the Show Message button
    Then the user should see the message "My pytest-bdd message"
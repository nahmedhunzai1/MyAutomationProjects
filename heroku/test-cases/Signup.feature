Feature: The signup feature
  Scenario: Verify if the user is able to signup successfully
    Given The user is on the signup page
    When The user enters valid signup details
    Then The user should be registered successfully

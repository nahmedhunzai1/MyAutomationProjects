Feature: The signin feature

  Background:
    Given The user is on the signin page

  Scenario Outline: Verify if the user is able to signin successfully
    When The user enters "<username>" and "secret_sauce"
    Then The user should be signed in successfully

    Examples:
      | username               |
      | standard_user          |
      | locked_out_user        |
      | problem_user           |
      | performance_glitch_user|
      | error_user             |
      | visual_user            |

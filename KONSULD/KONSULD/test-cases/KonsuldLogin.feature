Feature: sign steps
  Scenario: Verify user is able to sign in successfully
    Given User opens Konsuld URL-1
    When click Log In button-1
    And enter email and password-1
    And click Sign In button-1
    And Get the verfication code from mailosaurs inbox-1
    And enter it in the verification code section-1
    And click confirm-1
    Then user must login the app-1











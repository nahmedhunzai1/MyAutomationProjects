Feature:Sign Up
  @KonsuldWebPage
  Scenario: Verify the sign up is working properly
    When User opens Konsuld URL-2
    And Click Sign up button-2
    And Fill the sign up form with valid email-2
    And Acccept terms and conditions-2
    Then click create account button-2

  @KonsuldEmailVerification
  Scenario: Email verification
    When User opens gmail-2
    And Login account-2
    And Verify the message in the account-2
    And redirected to the kunsuld webiste-2







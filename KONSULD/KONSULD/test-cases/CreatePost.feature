Feature: Create Konsuldation

  @KonsuldLoginCreateKonsuldation
  Scenario: Verify user is able to Create Post successfully
    Given User opens Konsuld URL-3
    When click Log In button-3
    And enter email and password-3
    And click Sign In button-3
    And Get the verfication code from mailosaurs inbox-3
    And enter it in the verification code section-3
    And click confirm-3
    And user must login the app-3
    And User is present on the home page-3
    And User click Create Post button-3
    And Enter the title and description-3
    And Upload multiple videos-3
    And Upload multiple images-3
    And Add multiple URLs-3
    And Upload multiple documents-3
    And Click Create Post button and verify the success message-3
    Then The Post is created and it appears on home page-3
Feature: Create Konsuldation
  Scenario: Verify user is able to Create Konsuldation successfully
    Given User opens Konsuld URL-4
    When User click request konsuldation-4
    And Enter the title and description-4
    And Upload multiple videos-4
    And Upload multiple images-4
    And Add multiple URLs-4
    And Upload multiple documents-4
    And Add multiple specialitites-4
    And Add multiple focus Areas-4
    And Click Request Konsuldation button and verify the success message-4
    Then The Konsuldation is created and it appears on home page-4
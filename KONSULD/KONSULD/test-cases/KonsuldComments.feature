Feature: Comment
  @KonsuldLoginCreateKonsuldation
  Scenario: Verify user comment on posts successfully
    Given User opens Konsuld URL-5
    When click Log In button-5
    And enter email and password-5
    And click Sign In button-5
    And Get the verfication code from mailosaurs inbox-5
    And enter it in the verification code section-5
    And click confirm-5
    And user must login the app-5
    And User is present on the home page-5
    And User searches the other user #Oliver George#-5
    And Selects posts option from dropdown-5
    And Click through the first post appearing and navigate to post detail-5
    And User Likes and Comments on the post-5



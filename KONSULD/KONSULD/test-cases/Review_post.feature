Feature: Review on a Post or Konsuldation
  @CreaateKonsuldationForReview
  Scenario: Verify user is able to Review post or Konsuldation successfully
    Given Given User opens Konsuld URL-RP
    When click Log In button-RP
    And enter email and password-RP
    And click Sign In button-RP
    And Get the verfication code from mailosaurs inbox-RP
    And enter it in the verification code section-RP
    And click confirm-RP
    And user must login the app-RP
    And User is present on the home page-RP
    And User click request konsuldation-RP
    And Enter the title and description-RP
    And Upload multiple videos-RP
    And Upload multiple images-RP
    And Add multiple URLs-RP
    And Upload multiple documents-RP
    And Add multiple specialitites-RP
    And Add multiple focus Areas-RP
    And Click Request Konsuldation button and verify the success message-RP
    Then The Konsuldation is created and it appears on home page-RP



  @CommentKonsuldForReivew
  Scenario: Verify user is able to Review post or Konsuldation successfully
    Given Given User opens Konsuld URL-RP1
    When click Log In button-RP1
    And enter email and password-RP1
    And click Sign In button-RP11
    And Get the verfication code from mailosaurs inbox-RP1
    And enter it in the verification code section-RP1
    And click confirm-RP1
    And user must login the app-RP1
    And User is present on the home page-RP1
    And User navigates to the other users porfile-RP1
    Then Comments out the recent post-RP1


  @CLoseTheKonsuldForReview
  Scenario: Verify user is able to Review post or Konsuldation successfully
    Given Given User opens Konsuld URL-RP2
    When click Log In button-RP2
    And enter email and password-RP2
    And click Sign In button-RP2
    And Get the verfication code from mailosaurs inbox-RP2
    And enter it in the verification code section-RP2
    And click confirm-RP2
    And user must login the app-RP2
    And User is present on the home page-RP2
    And User navigates his own post-RP2
    Then User closes the post-RP2


  @PutReviewOnKonsuldation
  Scenario: Verify user is able to Review post or Konsuldation successfully
    Given User opens Konsuld URL-RP3
    When click Log In button-RP3
    And enter email and password-RP3
    And click Sign In button-RP3
    And Get the verfication code from mailosaurs inbox-RP3
    And enter it in the verification code section-RP3
    And click confirm-RP3
    And user must login the app-RP3
    And User is present on the home page-RP3
    And User navigates ratings-RP3
    Then User review the Konsuldation-RP3






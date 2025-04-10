Feature: Send Message to other user
  @KonsuldSendMessage
  Scenario: Verify that sending the message is working properly
    Given User opens Konsuld URL-sm
    When click Log In button-sm
    And enter email and password-sm
    And click Sign In button-sm
    And Get the verfication code from mailosaurs inbox-sm
    And enter it in the verification code section-sm
    And click confirm-sm
    And click the message option-sm
    And click Send New Message option-sm
    And click message option to first newtwork-sm
    And Enter a message and clock send button-sm



  @KonsuldReplyMessage
  Scenario: Verify user is able to reply the message-sm1
    Given User opens Konsuld URL-sm1
    When click Log In button-sm1
    And enter email and password-sm1
    And click Sign In button-sm1
    And Get the verfication code from mailosaurs inbox-sm1
    And enter it in the verification code section-sm1
    And click confirm-sm1
    And user must login the app-sm1
    And User is present on the home page-sm1
    And User opens messages-sm1
    And replies to the received message-sm1


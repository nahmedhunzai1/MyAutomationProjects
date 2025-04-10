Feature: Send Connect request
  Scenario: Verify user is able to send connect request successfully
    Given User opens Konsuld URL-6
    When user must login the app-6
    And User is present on the home page-6
    And User searches the other user #Oliver George#-6
    And Selects posts option from dropdown-6
    And Click other users profile-6
    And Click connect button-6
    And User opens Konsuld URL-7
    And user must login the app-7
    And User is present on the home page-7
    And User opens notification-7
    And Accepts connect requesst-7
    Then Disconnects  Request-7





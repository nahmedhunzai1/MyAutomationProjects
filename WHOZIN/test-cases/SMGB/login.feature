Feature: User Login
  Scenario: Check User section

   When user click user section
   Then User must go to users page


  Scenario: Check the date filter
    When user click on date filter
    And  user selects the desired date
# Background: Common Steps
#   Given launch chrome browser
#  When User goes to the login page
#  #step paremeters#
#  And Enter username "admin@scanmygolfball.com" and password "Rivers"
#  And Click on Login button
#
#
#  Scenario Outline: Successful Login
#    Given launch chrome browser
#    When User goes to the login page
#    #step paremeters#
#    And Enter username "<username>" and password "<password>"
#    And Click on Login button
#    Then User must login successfully to the dashboard page
#
#    Examples:
#      |username|password|
#      |admin@scanmygolfball.com|Rivers|










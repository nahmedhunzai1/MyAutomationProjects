Feature: User Login Step
  Background: Common Steps
     Given launched chrome browser3
     When User navigates to the login page3
     #step paremeters#
     And Enter username3 "admin@scanmygolfball.com" and password3 "Rivers"
     And Click on Login button3

  Scenario: Verify the remaining sections of the Admin Dashboard
    Given User is on the Admin Dashboard
    When User navigates to Scan per rate of playability section
    And Changes the from and to dates then the graph is working fine




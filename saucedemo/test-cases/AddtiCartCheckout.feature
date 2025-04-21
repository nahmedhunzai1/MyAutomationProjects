Feature: The Add to cart and checkout feature

  Background:
    Given The user is on the signin page

  Scenario Outline: Verify user is able to add the items in cart and complete checkout successfully
    When The user enters "<username>" and "secret_sauce"
    And The user should be signed in successfully
    And User must be able to search desired product
    And User navigate to the product detail
    And User add product to cart
    Then User completes the checkout successfuly


    Examples:
      | username               |
      | standard_user          |


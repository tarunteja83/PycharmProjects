Feature: Order Transaction
    Tests related to order details

  Scenario Outline: Verify order success message shown in details page
    Given place the item order with <username> and <password>
    And the user is on landing page
    When I login to the application <username> and <password>
    And navigate to orders page
    And select the orderid
    Then Signout the user
    Examples:
      | username                | password  |
      | tarunteja8383@gmail.com | taRuna@83 |
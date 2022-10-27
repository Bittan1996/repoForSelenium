Feature: Login
    """
        Login feature will test for successful and failed login attempts
    """

    Scenario: Success test for login
        Given I navigate to login page
        When I enter valid username and password
        And I click on Submit button
        Then login is successful

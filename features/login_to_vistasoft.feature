Feature: Login to VistaSoft Monitor IoT Solution
  Scenario: Login with valid credentials
    Given launch chrome
    And open vistasoft homepage
    When input email
    And input password
    And click login button
    Then verify successful login
    And close browser

Feature: Login to VistaSoft Monitor IoT Solution
  Scenario: Login with valid credentials
    Given launch browser "Chrome"
    And open vistasoft homepage
    When input email "dd_test_1@outlook.com"
    And input password "}krK,gdC6"
    And click login button
    Then verify successful login
    And close browser

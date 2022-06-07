Feature: View My User Account
  Scenario: Verify Username and Email
    Given launch browser "Chrome"
    And open vistasoft homepage
    When input email "dd_test_1@outlook.com"
    And input password "}krK,gdC6"
    And click login button
    And verify successful login
    And click user profile
    And select my user account
    Then verify name "test_1" and email "dd_test_1@outlook.com" is correct
    And close browser
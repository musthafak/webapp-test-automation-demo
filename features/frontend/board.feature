Feature: Trello Board Management

  Scenario: Create a Trello board
    Given I am on the Trello homepage
    When I click on create button
    And I select the board option
    And I enter the board name as "Project A"
    And I click on create board button
    Then I should see a new board with the name "Project A"
    And I have "3" lists on the board

  Scenario: Archive a list on Trello board
    Given I am on the Trello homepage
    And I create a board with name "Project B"
    And I have "3" lists on the board
    When I archive first list item
    Then I have "2" lists on the board

  Scenario: Delete a board on Trello
    Given I am on the Trello homepage
    And I create a board with name "Project C"
    When I permanently delete the board
    Then I dont have "Project C" board in my workspace

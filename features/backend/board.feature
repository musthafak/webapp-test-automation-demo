Feature: Trello Boards REST API

  Scenario: Create a Trello board
    Given I have a valid API key and token
    When I send a POST request to "/boards" with the payload:
      """
      {
        "name": "Project A"
      }
      """
    Then the response status code should be 200
    And the response body should contain the board ID
    And the board should be created successfully

  Scenario: View a Trello board
    Given I have a valid API key and token
    And I have a board ID
    When I send a GET request to "/boards/{boardId}"
    Then the response status code should be 200
    And the response body should contain the board details

  Scenario: Update a Trello board
    Given I have a valid API key and token
    And I have a board ID
    When I send a PUT request to "/boards/{boardId}" with the payload:
      """
      {
        "name": "Project A - Updated"
      }
      """
    Then the response status code should be 200
    And the board name should be updated to "Project A - Updated"

  Scenario: Delete a Trello board
    Given I have a valid API key and token
    And I have a board ID
    When I send a DELETE request to "/boards/{boardId}"
    Then the response status code should be 200
    And the board should be deleted successfully

  Scenario: Attempt to create a Trello board without a name
    Given I have a valid API key and token
    When I send a POST request to "/boards" with the payload:
      """
      {
        "name": ""
      }
      """
    Then the response status code should be 400
    And the response body should contain "invalid value"

  Scenario: Attempt to view a non-existing Trello board
    Given I have a non-existing board ID
    When I send a GET request to "/boards/{nonExistingBoardId}"
    Then the response status code should be 400
    And the response body should contain "invalid id"

  Scenario: Attempt to update a non-existing Trello board
    Given I have a non-existing board ID
    When I send a PUT request to "/boards/{nonExistingBoardId}" with the payload:
      """
      {
        "name": "Project A - Updated"
      }
      """
    Then the response status code should be 400
    And the response body should contain "invalid id"

  Scenario: Attempt to delete a non-existing Trello board
    Given I have a non-existing board ID
    When I send a DELETE request to "/boards/{nonExistingBoardId}"
    Then the response status code should be 400
    And the response body should contain "invalid id"

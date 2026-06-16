Feature: Create Post API

  Scenario: Successfully create a new post
    Given user has valid post payload
    When user sends POST request to create post
    Then response status code should be 201
    And response should contain id
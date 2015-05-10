Feature: behave_as

  Test calling behave_as on a step

  Scenario: Step callbacks
    Given I emit a step event of "A"
    And I emit a step event for each letter in "BCDE"
    # Last two brackets are from the current example
    Then the step event sequence should be "{[A]}{[{[B]}{[C]}{[D]}{[E]}]}{["
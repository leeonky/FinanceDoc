Feature: Compute factorial
	Scenario: Factorial of 0
		Given I have the number 0
		When I compute its factorial
		Then I see the number 1

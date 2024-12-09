Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select the 0 option for element "#decoder-setting"
    When I select the 1 option for element "#shift-amount"
    When I set "Test" to the inputfield "#letters"
    When I click on the element "#submit"
    Then I expect that message is encoded/decoded as "Uftu"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    When I select the 1 option for element "#decoder-setting"
    When I select the 1 option for element "#shift-amount"
    When I set "Uftu" to the inputfield "#letters"
    When I click on the element "#submit"
    Then I expect that message is encoded/decoded as "Test"

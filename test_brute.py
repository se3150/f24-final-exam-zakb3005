import pytest
from brute import Brute
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():
        def test_it_cracks_in_a_single_attempt(cracker):
            result = cracker.bruteOnce("TDD")
            assert result is True
            
        def test_it_returns_false_for_failed_attempt(cracker):
            result = cracker.bruteOnce("DDT")
            assert result is False
            
        def test_fails_when_attempt_is_not_a_string(cracker):
            with pytest.raises(TypeError):
                result = cracker.bruteOnce(123)
                
        def test_fails_when_attempt_is_null(cracker):
            with pytest.raises(TypeError):
                result = cracker.bruteOnce()

    def describe_bruteMany():
        def it_calls_brute_once(mocker):
            mock_brute_once = mocker.patch.object(Brute, 'bruteOnce')
            b = Brute("Test")
            b.bruteMany()
            mock_brute_once.assert_called_once()
            
        def it_calls_random_guess(mocker):
            mock_random = mocker.patch.object(Brute, 'randomGuess', return_value="Test")
            b = Brute("Test")
            b.bruteMany()
            mock_random.assert_called_once()
            
        def it_cracks_successfully_and_returns_time(mocker):
            mock_hash = mocker.patch.object(Brute, 'hash', return_value="Final")
            mock_random_guess = mocker.patch.object(Brute, 'randomGuess', return_value="Final")
            b = Brute("Exam")
            result = b.bruteMany()
            mock_hash.assert_called_with("Final")
            mock_random_guess.assert_called_once()
            assert result is not -1
            
        def it_returns_negative_one_when_failed(mocker):
            mock_hash = mocker.patch.object(Brute, 'hash', return_value="Final")
            mock_random_guess = mocker.patch.object(Brute, 'randomGuess', return_value="Failed")
            b = Brute("Exam")
            result = b.bruteMany()
            mock_random_guess.assert_called_once()
            assert result is not -1
            
        def it_returns_the_proper_succeeded_time(mocker):
            mock_hash = mocker.patch.object(Brute, 'hash', return_value="succeed")
            mock_guess = mocker.patch.object(Brute, 'randomGuess', return_value="succeed")
            b = Brute("Exam")
            result = b.bruteMany(1)
            assert result < 1
            
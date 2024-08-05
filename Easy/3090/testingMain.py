import pytest
import main_file as code

@pytest.mark.parametrize("given_input,expected_output",[('bcbbbcba',4),('aaaa',2),('ccbcb',4),('abcdabcd',8)])
                         
def test_candy(given_input,expected_output):
    assert code.Solution().maximumLengthSubstring(given_input) == expected_output
  
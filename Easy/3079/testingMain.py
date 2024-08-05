import pytest
import main_file as code

@pytest.mark.parametrize("given_input,expected_output",[('abcdefgh',8),('abcdabcd',4),('aabcaa',3),('aaaaaaa',1)])
                         
def test_candy(given_input,expected_output):
    assert code.minPathSum(given_input) == expected_output
  
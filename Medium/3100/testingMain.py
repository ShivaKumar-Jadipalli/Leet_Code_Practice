import pytest
import main_file as code

@pytest.mark.parametrize("given_input,given_input_1,expected_output",[(10,3,13),(13,6,15)])
                         
def test_candy(given_input,given_input_1,expected_output):
    assert code.Solution().maxBottlesDrunk(given_input,given_input_1) == expected_output

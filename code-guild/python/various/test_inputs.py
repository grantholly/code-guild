import mock
import inputs

def test_get_input():
    with mock.patch('__builtin__.raw_input', return_value = 'grant'):
	assert get_input() == 'hello grant'

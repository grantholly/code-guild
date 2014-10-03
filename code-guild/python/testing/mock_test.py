import mock

def s():
    word = raw_input('words')
    return word

def test_s():
    with mock.patch('__builtin__.raw_input', return_value='y'):
	assert s() == test_s()



import io
import pathlib
import sys

from input_ import input_
from test_public import test_basic
from test_public import test_eof
from test_public import test_eof_with_prompt
from test_public import test_prompt_flushed

def test_input():
	print('start test_input:')
	inp = io.StringIO('test_input\n')
	out = io.StringIO()
	ret = input_('prompt', inp, out)
	print('ret: ', ret)
	print('end test_input')
    #assert out.getvalue() == (prompt or '')

if __name__ == "__main__":
	#input_('login: ')
	#out = io.StringIO()
	#input_('login: ', None, out)
	#inp = io.StringIO()
	#input_('login: ', inp, None)

	test_basic('prompt', 'user_input')
	test_eof()
	test_eof_with_prompt()
	test_prompt_flushed('.')
	#test_input()

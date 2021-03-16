import sys
import typing as tp


def input_(prompt: tp.Optional[str] = None,
           inp: tp.Optional[tp.IO[str]] = None,
           out: tp.Optional[tp.IO[str]] = None) -> tp.Optional[str]:
    """Read a string from `inp` stream. The trailing newline is stripped.

    The `prompt` string, if given, is printed to `out` stream without a
    trailing newline before reading input.

    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), return None.

    `inp` and `out` arguments are optional and should default to `sys.stdin`
    and `sys.stdout` respectively.
    """
    if prompt is None:
    	return None

    if out == None:
    	sys.stdout.write(prompt)
    	sys.stdout.flush()
    	if inp != None:
            line = inp.readline()
            line = line.rstrip('\n')
            if line == '':
                return None
            return line
    	else:
            line = sys.stdin.readline()
            line = line.rstrip('\n')
            if line == '':
                return None
            return line
    else:
    	out.write(prompt)
    	out.flush()
    	if inp != None:
    		line = inp.readline()
    		line = line.rstrip('\n')
    		if line == '':
    			return None
    		return line
    	else:
            line = sys.stdin.readline()
            line = line.rstrip('\n')
            if line == '':
                return None
            return line

  

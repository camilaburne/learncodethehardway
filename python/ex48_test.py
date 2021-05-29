from nose.tools import *
from ex48 import scan


def test_verbs():
    assert_equal(scan('go'), [('verbs','go')])

    result = scan('go kill eat')
    assert_equal(result, [('verbs','go'),
                         ('verbs','kill'),
                         ('verbs','eat')]
                 )

test_verbs()

import pytest
from  API import calculate
#API import calculate

def testcalc():
    # given
    c = 1
    d = 2
    # when
    actual = calculate(c,d)
    # then
    output = c + d
    assert(output == 3)


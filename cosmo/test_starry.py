import starry
import pytest
import hypothesis.strategies as st
from hypothesis import given

def test_1():
    assert starry.dictator([1,2,3,4], ['a','b']) == {1:'a',2:'b',3:None,4:None}

def test_2():
    assert starry.dictator([1,2], []) == {1:None,2:None}

def test_3():
    assert starry.dictator([], []) == {}

@given(st.lists(st.integers()), st.lists(st.integers()))
def test_hyp_small(x, y):
	assert len(starry.dictator(x, y)) == len(dict.fromkeys(x, None))

@given(st.sets(st.integers()), st.sets(st.integers()))
def test_hyp_xxxl(keys, values):
	keys = list(keys)
	values = list(values)

	res = starry.dictator(keys, values)

	if len(keys) < len(values):
		values = values[0:len(keys):]
	
	if len(values) < len(keys):
		for i in range(len(keys) - len(values)):
			values.append(None)
	
	assert list(res.keys()) == keys
	assert list(res.values()) == values

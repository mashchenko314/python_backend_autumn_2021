import pytest
from my_classes.custom_meta import CustomClass

@pytest.fixture
def inst():
    return CustomClass()

def test_should_cause_exc_about_accessing_attributes_without_prefix(inst):
    with pytest.raises(AttributeError) as exc:
        inst.line()
    assert exc.type == AttributeError
    with pytest.raises(AttributeError) as exc:
        print(inst.x)
    assert exc.type == AttributeError
    with pytest.raises(AttributeError) as exc:
        print(inst.val)
    assert exc.type == AttributeError

def test_should_add_prefix(inst):
    assert inst.custom_line() == 100
    assert inst.custom_x == 50
    assert inst.custom_val == 99

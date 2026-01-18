from app.main import get_human_age

def test_should_return_list_with_0():
    cat_age = 13
    dog_age = 12
    assert get_human_age(cat_age, dog_age) == [0, 0]


def test_should_return_list_with_1():
    pass


def test_should_return_list_with_more_then_2():
    pass


def test_should_return_list_with_different_values():
    pass

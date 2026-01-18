from app.main import get_human_age

def test_animals_yonger_then_15_years():
    cat_age = 13
    dog_age = 12
    assert get_human_age(cat_age, dog_age) == [0, 0]

import pytest


from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age,  result",
    [
        pytest.param(13, 12, [0, 0], id="animal years less then 15 years"),
        pytest.param(15, 16, [1, 1],
                     id="animal years equell or more 15 but less 24"),
        pytest.param(24, 24, [2, 2],
                     id="animal years equell or more 24 but less 32"),
        pytest.param(28, 29, [3, 3], id="animal years equell or more 32"),
        pytest.param(32, 16, [4, 1], id="animal years equell different value"),
    ]
)
def test_should_return_list_with_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result

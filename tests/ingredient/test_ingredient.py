from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    first = Ingredient("Banana")
    second = Ingredient("Pitaya")
    third = Ingredient("Banana")

    assert first.name == "Banana"
    assert first.restrictions == set()

    assert hash(first) != hash(second)
    assert hash(first) == hash(third)

    assert first == third
    assert first != second

    assert repr(first) == "Ingredient('Banana')"

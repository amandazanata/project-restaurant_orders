import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    first_dish = Dish("Banoffe", 23.90)
    second_dish = Dish("Banoffe", 23.90)
    third_dish = Dish("Bolo de Cenoura", 25.90)

    assert first_dish.name == "Banoffe"
    assert first_dish.price == 23.90
    assert first_dish.recipe == {}

    assert hash(first_dish) != hash(third_dish)
    assert hash(first_dish) == hash(second_dish)

    assert first_dish == second_dish
    assert first_dish != third_dish

    assert repr(first_dish) == "Dish('Banoffe', R$23.90)"

    with pytest.raises(TypeError):
        Dish("Prato inválido", "string")

    with pytest.raises(ValueError):
        Dish("Prato inválido 2", -9)

    first_ingredient = Ingredient("Banana")
    second_ingredient = Ingredient("Caramelo")
    first_dish.add_ingredient_dependency(first_ingredient, 2)
    assert first_ingredient in first_dish.recipe
    assert second_ingredient not in first_dish.recipe
    assert first_dish.recipe[first_ingredient] == 2

    third_ingredient = Ingredient("farinha")
    first_dish.add_ingredient_dependency(third_ingredient, 1)
    assert first_dish.get_restrictions() == {Restriction.GLUTEN}
    assert first_dish.get_ingredients() == {first_ingredient, third_ingredient}

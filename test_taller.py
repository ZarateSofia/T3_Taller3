import main
import pytest

#calculate Special Discount
@pytest.mark.parametrize("total_cost, expected_discount", [
    (100, 0),
    (250, 20),
    (450, 50),
    (200, 0),
    (400, 20),
    (600, 50)
])
def test_calculate_special_discount(total_cost, expected_discount):
    result = main.calculate_special_discount(total_cost)
    assert result == expected_discount, f"Falló con entrada {total_cost}: resultado {result}, esperado {expected_discount}"

@pytest.mark.parametrize("group_size, membership_cost, expected_discount", [
    (2, 100, 10),
    (3, 150, 15),
    (1, 200, 0),
    (5, 300, 30),
    (2, 50, 5)
])
def test_calculate_group_discount(group_size, membership_cost, expected_discount):
    result = main.calculate_group_discount(group_size, membership_cost)
    assert result == expected_discount, f"Falló con entrada (group_size={group_size}, membership_cost={membership_cost}): resultado {result}, esperado {expected_discount}"

@pytest.mark.parametrize("plan, features, expected_cost", [
    ("Basic", ["Personal training sessions"], 125),
    ("Premium", ["Group classes", "Specialized training programs"], 300),
    ("Family", ["Personal training sessions", "Group classes"], 130),
    ("Basic", [], 100),
    ("Premium", ["Personal training sessions"], 125)
])
def test_calculate_total_cost(plan, features, expected_cost):
    result = main.calculate_total_cost(plan, features)
    assert result == expected_cost, f"Falló con entrada (plan={plan}, features={features}): resultado {result}, esperado {expected_cost}"

def test_calculate_premium_surcharge():
    total_cost = 100
    expected_surcharge = total_cost * 0.15
    result = main.calculate_premium_surcharge(total_cost)
    assert result == pytest.approx(expected_surcharge), f"Falló con total_cost={total_cost}: resultado {result}, esperado {expected_surcharge}"


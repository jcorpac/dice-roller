import pytest
from dice_roller.logic import add_logic, roll_die_logic, roll_ability_score_logic, roll_d20_logic, roll_dice_logic

def test_add():
    assert add_logic(1, 2) == 3
    assert add_logic(-1, 1) == 0

def test_roll_die():
    result = roll_die_logic(6)
    assert 1 <= result <= 6
    
    result = roll_die_logic(20)
    assert 1 <= result <= 20

def test_roll_ability_score():
    # Statistical test is hard, but we can check bounds
    for _ in range(100):
        score = roll_ability_score_logic()
        assert 3 <= score <= 18

def test_roll_d20():
    # Test normal roll
    res = roll_d20_logic(modifier=5)
    assert 6 <= res["total"] <= 25
    assert res["modifier"] == 5
    
    # Test advantage (mocking would be better but simple logic check)
    res = roll_d20_logic(advantage=True)
    assert 1 <= res["base_roll"] <= 20
    assert "Advantage" in res["reason"]

    # Test disadvantage
    res = roll_d20_logic(disadvantage=True)
    assert 1 <= res["base_roll"] <= 20
    assert "Disadvantage" in res["reason"]

def test_roll_dice():
    # Test 2d6 + 3
    res = roll_dice_logic(count=2, sides=6, modifier=3)
    assert 5 <= res["total"] <= 15
    assert len(res["rolls"]) == 2
    assert res["modifier"] == 3

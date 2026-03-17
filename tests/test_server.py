from dice_roller.main import add, roll_die, roll_ability_score, roll_d20, roll_dice

def test_add_tool():
    assert add.fn(1, 2) == 3

def test_roll_die_tool():
    res = roll_die.fn(6)
    assert 1 <= res <= 6

def test_roll_ability_score_tool():
    score = roll_ability_score.fn()
    assert 3 <= score <= 18

def test_roll_d20_tool():
    res = roll_d20.fn(modifier=5)
    assert 6 <= res["total"] <= 25

def test_roll_dice_tool():
    res = roll_dice.fn(count=2, sides=6, modifier=3)
    assert 5 <= res["total"] <= 15

def add_logic(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

def roll_die_logic(sides: int = 6) -> int:
    """Roll a die with the specified number of sides."""
    import random
    return random.randint(1, sides)

def roll_ability_score_logic() -> int:
    """Roll 4d6 and drop the lowest die to generate an ability score."""
    import random
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.sort()
    return sum(rolls[1:])

def roll_d20_logic(modifier: int = 0, advantage: bool = False, disadvantage: bool = False) -> dict:
    """Roll a d20 with optional modifier, advantage, or disadvantage."""
    import random
    
    roll1 = random.randint(1, 20)
    roll2 = random.randint(1, 20)
    
    if advantage and not disadvantage:
        base_roll = max(roll1, roll2)
        reason = "Advantage (max of {}, {})".format(roll1, roll2)
    elif disadvantage and not advantage:
        base_roll = min(roll1, roll2)
        reason = "Disadvantage (min of {}, {})".format(roll1, roll2)
    else:
        base_roll = roll1
        reason = "Normal roll"
        
    total = base_roll + modifier
    return {
        "total": total,
        "base_roll": base_roll,
        "modifier": modifier,
        "reason": reason
    }

def roll_damage_logic(count: int, sides: int, modifier: int = 0) -> dict:
    """Roll damage (e.g., 2d6 + 3)."""
    import random
    rolls = [random.randint(1, sides) for _ in range(count)]
    total = sum(rolls) + modifier
    return {
        "total": total,
        "rolls": rolls,
        "modifier": modifier
    }

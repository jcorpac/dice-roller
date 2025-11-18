from fastmcp import FastMCP
from dice_roller.logic import (
    add_logic,
    roll_die_logic,
    roll_ability_score_logic,
    roll_d20_logic,
    roll_damage_logic,
)

# Initialize the FastMCP server
mcp = FastMCP("MCP Dice Roller")

# MCP Tools
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return add_logic(a, b)

@mcp.tool()
def roll_die(sides: int = 6) -> int:
    """Roll a die with the specified number of sides."""
    return roll_die_logic(sides)

@mcp.tool()
def roll_ability_score() -> int:
    """Roll 4d6 and drop the lowest die to generate an ability score."""
    return roll_ability_score_logic()

@mcp.tool()
def roll_d20(modifier: int = 0, advantage: bool = False, disadvantage: bool = False) -> dict:
    """Roll a d20 with optional modifier, advantage, or disadvantage."""
    return roll_d20_logic(modifier, advantage, disadvantage)

@mcp.tool()
def roll_damage(count: int, sides: int, modifier: int = 0) -> dict:
    """Roll damage (e.g., 2d6 + 3)."""
    return roll_damage_logic(count, sides, modifier)

if __name__ == "__main__":
    mcp.run()

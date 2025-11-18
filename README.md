# Dice Roller

A FastMCP dice roller project.

## Usage

Run the server:
```bash
uv run fastmcp run src/dice_roller/main.py
```

## Features

- **Basic Math**: `add(a, b)`
- **Simple Dice**: `roll_die(sides)`
- **D&D Features**:
    - `roll_ability_score()`: Rolls 4d6 drop lowest.
    - `roll_d20(modifier, advantage, disadvantage)`: Rolls a d20 with modifiers and mechanics.
    - `roll_damage(count, sides, modifier)`: Rolls damage dice.

## Testing

Run tests with:
```bash
uv run pytest
```

## Docker

Build and run with Docker:
```bash
docker build -t fastmcp-app .
docker run --rm fastmcp-app
```

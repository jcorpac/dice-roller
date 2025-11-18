# MCP Dice Roller

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
docker build -t mcp-dice-roller .
docker run --rm mcp-dice-roller
```

## Connect to Chat Apps

To use this MCP server with a client like Claude Desktop, add the following configuration to your `claude_desktop_config.json`:

### Local Development
```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [
        "run",
        "fastmcp",
        "run",
        "src/dice_roller/main.py"
      ]
    }
  }
}
```

### Docker
```json
{
  "mcpServers": {
    "dice-roller": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "mcp-dice-roller"
      ]
    }
  }
}
```

### Ollama
You can use this MCP server with Ollama by configuring it as a tool provider.

#### Local Development
```bash
ollama run llama3.2 --mcp "uv run fastmcp run src/dice_roller/main.py"
```

#### Docker
```bash
ollama run llama3.2 --mcp "docker run -i --rm mcp-dice-roller"
```

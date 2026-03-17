# Snake Water Gun

A Python terminal game — the desi version of Rock Paper Scissors.

## Rules

| Your pick | Beats     |
|-----------|-----------|
| Snake     | Water     |
| Water     | Gun       |
| Gun       | Snake     |

## Usage
```bash
python snake_water_gun.py
```

You'll be prompted to type your choice. The computer picks randomly, and the
result prints immediately.

## Example
```
Enter your choice (snake, water, gun): snake
You chose: snake
Computer chose: water
You win!
```

## Requirements

No external libraries. Just Python 3.

## What I Learned

- Writing game logic with `if-else` conditions
- Separating logic into functions
- Using `random.choice()` for computer moves
- Taking and normalizing user input with `.lower()`
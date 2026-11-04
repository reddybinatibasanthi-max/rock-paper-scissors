# Rock Paper Scissors

A simple command-line Rock Paper Scissors game written in Python. You play against the computer, which picks its move at random.

## Features

- Play against the computer in the terminal
- Input is case-insensitive (`Rock`, `ROCK` and `rock` all work)
- Friendly message for invalid choices
- No external libraries needed

## Requirements

- Python 3.6 or higher

## How to Run

1. Clone this repository:
   ```
   git clone https://github.com/reddybinatibasanthi-max/rock-paper-scissors.git
   cd rock-paper-scissors
   ```
2. Run the game:
   ```
   python rock_paper_scissors.py
   ```
   On some systems you may need to use `python3` instead of `python`.

## How to Play

Type `rock`, `paper`, or `scissors` when prompted. The computer picks at random and the winner is shown.

| Your move | Beats    |
|-----------|----------|
| Rock      | Scissors |
| Paper     | Rock     |
| Scissors  | Paper    |

## Example

```
Enter your choice (rock, paper, scissors): rock
You chose rock, Computer chose scissors
Rock smashes scissors! You win!
```

## Possible Improvements

- Play multiple rounds with a running score
- Ask "Play again?" after each round
- Add a graphical interface

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

R Binati Basanthi ([@reddybinatibasanthi-max](https://github.com/reddybinatibasanthi-max))

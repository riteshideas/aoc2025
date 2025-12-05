# Advent of Code 2025

This is the repository for the [advent of code 2025](https://adventofcode.com/2025). This repository houses the solutions advent of code labeled by the `day{Day}p{Part}.py` eg `day05p2.py`

### How to run
I have created 2 shell scripts to assist in downloading the data from the advent of code website.</br>The `aoc.sh` downloads the puzzle input while the `aot.sh` (testing data) uses the data from `testcase.txt`. For the `aoc.sh` script to work you will need to login to the advent of code website and obtain your session cookie (`Inspect Element > Application > Cookies > https://adventofcode.com > session`). Afterwards save this into your environment variable as `$AdventOfCode`. Obtaining the cookie is essential since the puzzle input is different between users. Then use the command `./aoc.sh DAY PART`, if you would like profilling enables, install the [py-spy](https://pypi.org/project/py-spy/0.1.3/) module and use the command `./aoc.sh DAY PART --profile`. Same with the `aot.sh`. Profiles will be saved to `profiles` folder
##### Example Commands
```sh
./aoc.sh 5 2
./aot.sh 3 1
./aoc.sh 11 2
```
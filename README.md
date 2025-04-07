# Advent of Code

![AoC](aoc.png)

## Completion

- 2015 : [TODO] Haskell.
- 2016 : [TODO] Julia.
- 2017 : [TODO] Nim.
- 2018 : [TODO] Zig.
- 2019 : 17/25 days complete in Python 3.
- 2020 : 25/25 days complete in Python 3. [DONE]
- 2021 : 14/25 days complete in Rust 2021.
- 2022 : 12/25 days complete in Rust 2021.
- 2023 : 20/25 days complete in Golang 1.21.
- 2024 : 9/25 days complete in CSharp 9.0.
- 2025 : [TODO] Kotlin.

97 total days finished.

8400+ SLOC in total.

## Requirements

- Python >=3.10 installed.
  - "python3" as a recognized terminal command.

- Rust >=2021 installed.
  - "cargo" as a recognized terminal command.

- Golang >=1.21 installed.
  - "go" as a recognized terminal command.

- CSharp >=9.0 installed.
  - "dotnet" as a recognized terminal command.

## Directory

The years written in Python contain the following structure:

- /input/day\*.txt : Holds the inputs in text files.
- /day\*.py : Code that solves both parts of the day from the input held in "/input".
- /timing.py : Code that times every solution for both parts and prints the average.

The years written in Rust contain the following structure:

- /input/day\*.txt : Holds the inputs in text files.
- /src/day\*.rs : Code that solves both parts of the day from the input held in "/input".
- /src/timing.rs : Code that times every solution for both parts and prints the average.
- /src/read.rs : Code that provides for various utility and misc functions.

The years written in Golang contain the following structure:

- /input/day\*.txt : Holds the inputs in text files.
- /day\*.go : Code that solves both parts of the day from the input held in "/input".
- /timing.go : Code that times every solution for both parts and prints the average.
- /tool.go : Code that provides for various utility and misc functions.

The years written in CSharp contain the following structure:

- /input/day\*.txt : Holds the inputs in text files.
- /day\*.cs : Code that solves both parts of the day from the input held in "/input".
- /timing.cs : Code that times every solution for both parts and prints the average.
- /tool.cs : Code that provides for various utility and misc functions.

Additionally, year 2019 includes the following file:

- /2019/intcode.py : The newer implementation of an Intcode computer.
- /2019/intcodeold.py : The older implementation of an Intcode computer.
- /2019/verify.py : Verify that every Intcode day remains unchanged.

In the top level directory:

- [WINDOWS] start.bat : Starts the "run.bat" file.
- [WINDOWS] run.bat : Runs the timing file for every year.
- [LINUX] run.sh : Runs the timing file for every year.

- template : Simple templates for the Python and Rust solutions.

## License

https://creativecommons.org/licenses/by/4.0/

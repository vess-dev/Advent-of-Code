#!/bin/bash
echo -ne "\033]0;unning Advent...\007"
cd 2019 ; python -B timing.py ; cd ..
cd 2020 ; python -B timing.py ; cd ..
cd 2021 ; cargo run --release ; cd ..
cd 2022 ; cargo run --release ; cd ..
cd 2023 ; go run . ; cd ..
cd 2024 ; dotnet run aoc2024.csproj ; cd ..
read -n 1 -s -p "Press any key to continue"
exit
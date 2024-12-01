@echo off
title Running Advent...
cd 2019 & python -B timing.py & cd ..
cd 2020 & python -B timing.py & cd ..
cd 2021 & cargo run --release & cd ..
cd 2022 & cargo run --release & cd ..
cd 2023 & go run . & cd ..
cd 2024 & dotnet run aoc2024.csproj & cd ..
pause
exit
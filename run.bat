@echo off
title Running Advent...
cls
python -B %~dp0/2019/timing.py
python -B %~dp0/2020/timing.py
cargo run --manifest-path=%~dp0/2021/Cargo.toml
pause
exit
#!/bin/bash
clear
python -B "./2019/timing.py"
python -B "./2020/timing.py"
cargo run --manifest-path="./2021/Cargo.toml"
cargo run --manifest-path="./2022/Cargo.toml"
read -n 1 -s -p "Press any key to continue"
exit
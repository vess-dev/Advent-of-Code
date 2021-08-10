@echo off
title Running file...
cls
cd "2020"
python -B %~dp0/timing.py
pause
exit
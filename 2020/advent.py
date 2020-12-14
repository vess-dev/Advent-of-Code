import time

import advent

import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14

def clock(advent_day, test_count):
    time_total = 0
    for temp_step in range(test_count):
        time_before = time.time()
        advent_day.run()
        time_total += time.time() - time_before
    return time_total

def run():
    advent_list = [day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14]
    test_count = 10
    time_total = 0
    if test_count:
        for temp_py in advent_list:
            print("Day", temp_py.day_num, ":", temp_py.run())
            time_next = clock(temp_py, test_count)
            print(test_count, "trials of day", temp_py.day_num, ":", time_next / test_count, "\n")
            time_total += time_next
        print(test_count, "trials of all, averages:", time_total / test_count, "\n")
    else:
        for temp_py in advent_list:
            print("Day", temp_py.day_num, ":", temp_py.run())
    
if __name__ == "__main__":
    advent.run()
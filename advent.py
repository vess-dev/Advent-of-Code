import time

import advent
import advent1
import advent2
import advent3
import advent4
import advent5

def clock(advent_day, time_tests):
    time_total = 0
    for temp_step in range(time_tests):
        time_before = time.time()
        advent_day.run()
        time_total += time.time() - time_before
    return time_total

def run(advent_list, time_tests):
    time_total = 0
    day_num = 1
    for temp_py in advent_list:
        print("Day", day_num, ":", temp_py.run())
        time_next = clock(temp_py, time_tests)
        print(time_tests, "trials of day", day_num, ":", time_next / time_tests, "\n")
        time_total += time_next
        day_num += 1
    print(time_tests, "trials of all :", time_total / time_tests, "\n")

if __name__ == "__main__":
    advent_list = [advent1, advent2, advent3, advent4, advent5]
    time_tests = 10
    advent.run(advent_list, time_tests)
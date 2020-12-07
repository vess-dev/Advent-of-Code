import time

import advent

import advent1
import advent2
import advent3
import advent4
import advent5
import advent6
import advent7

def clock(advent_day, test_count):
    time_total = 0
    for temp_step in range(test_count):
        time_before = time.time()
        advent_day.run()
        time_total += time.time() - time_before
    return time_total

def run(advent_list, test_count):
    day_num = 1
    time_total = 0
    for temp_py in advent_list:
        print("Day", day_num, ":", temp_py.run())
        time_next = clock(temp_py, test_count)
        print(test_count, "trials of day", day_num, ":", time_next / test_count, "\n")
        time_total += time_next
        day_num += 1
    print(test_count, "trials of all averages:", time_total / test_count, "\n")

if __name__ == "__main__":
    advent_list = [advent1, advent2, advent3, advent4, advent5, advent6, advent7]
    test_count = 3
    advent.run(advent_list, test_count)
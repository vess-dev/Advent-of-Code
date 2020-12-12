import time

import advent

import advent1
import advent2
import advent3
import advent4
import advent5
import advent6
import advent7
import advent8
import advent9
import advent10
import advent11
import advent12

def clock(advent_day, test_count):
    time_total = 0
    for temp_step in range(test_count):
        time_before = time.time()
        advent_day.run()
        time_total += time.time() - time_before
    return time_total

def run():
    advent_list = [advent1, advent2, advent3, advent4, advent5, advent6, advent7, advent8, advent9, advent10, advent11, advent12]
    test_count = 3
    time_total = 0
    if test_count:
        for temp_py in advent_list:
            print("Day", temp_py.day_num, ":", temp_py.run())
            time_next = clock(temp_py, test_count)
            print(test_count, "trials of day", temp_py.day_num, ":", time_next / test_count, "\n")
            time_total += time_next
        print(test_count, "trials of all averages:", time_total / test_count, "\n")
    else:
        for temp_py in advent_list:
            print("Day", temp_py.day_num, ":", temp_py.run())
    
if __name__ == "__main__":
    advent.run()
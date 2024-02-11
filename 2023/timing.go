package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

type TLIST_SIG = []func()(any,any)
var TDAY_LIST = TLIST_SIG{
	day1, day2, day3, day4, day5, day6, day7, day8, day9, day10, day11, day12, day13, day14,
}

func ttime(in_list TLIST_SIG) {
	test_count := 10
	time_total := time.Now()
	for itr_index, itr_func := range in_list {
		time_now := time.Now()
		var test_return [2]any
		var since_test time.Duration
		for itr_test := 0; itr_test < test_count; itr_test++ {
			test_return[0], test_return[1] = itr_func()
		}
		since_test += time.Since(time_now)
		fmt.Printf("Day %v: (%v, %v)\n", itr_index+1, test_return[0], test_return[1])
		since_testavg := since_test.Seconds() / float64(test_count)
		fmt.Printf("%v trials of day %v: %.7fs\n\n", test_count, itr_index+1, since_testavg)
	}
	since_start := time.Since(time_total)
	since_startavg := since_start.Seconds() / float64(test_count)
	fmt.Printf("%v trials of all, averages: %.7f seconds.\n", test_count, since_startavg)
}

func main() {
	arg_len := len(os.Args)
	if arg_len == 2 {
		int_data, int_error := strconv.Atoi(os.Args[1])
		tcheck(int_error)
		fmt.Println(TDAY_LIST[int_data-1]())
	} else if (arg_len == 3) && (os.Args[1] == "t") {
		int_data, int_error := strconv.Atoi(os.Args[2])
		tcheck(int_error)
		one_list := TLIST_SIG{TDAY_LIST[int_data-1]}
		ttime(one_list)
	} else {
		ttime(TDAY_LIST)
	}
}
package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

var day_list = []func()(any,any){
	day1, day2, day3, day4, day5, day6, day7,
}

func ttime() {
	test_count := 10
	time_total := time.Now()
	for itr_index, itr_func := range day_list {
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
	if len(os.Args) >= 2 {
		int_data, int_error := strconv.Atoi(os.Args[1])
		tcheck(int_error)
		fmt.Println(day_list[int_data-1]())
	} else {
		ttime()
	}
}
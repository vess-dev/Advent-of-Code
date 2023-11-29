package main

import (
	"fmt"
	"time"
)

func check(in_error error) {
	if in_error != nil {
		panic(in_error)
	}
}

func use(val_list ...any) {
    for _, itr_val := range val_list {
        _ = itr_val
    }
}

func main() {
	day_list := []func()(any,any){day1}
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
		fmt.Printf("Day %v: %v\n", itr_index+1, test_return)
		fmt.Printf("%v trials of day %v: %.7fs\n\n", test_count, itr_index+1, since_test.Seconds() / float64(test_count))
	}
	since_start := time.Since(time_total)
	fmt.Printf("%v trials of all, averages: %.7f seconds.\n", test_count, since_start.Seconds() / float64(test_count))
}
package main

import (
	"strings"
	"sync"
)

type d12Record struct {
	list []string
	verify []int
}

func d12clean(in_raw string) ([]d12Record, []d12Record) {
	string_list := strings.Split(in_raw, "\n")
	record_list := make([]d12Record, len(string_list))
	expand_list := make([]d12Record, len(string_list))
	for temp_idx, temp_record := range string_list {
		pair_list := strings.Split(temp_record, " ")
		int_list := strings.Split(pair_list[1], ",")
		verify_list := tcast(int_list)
		record_list[temp_idx] = d12Record{strings.Split(pair_list[0], ""), verify_list}
		expand_string := strings.Split(strings.TrimRight(strings.Repeat(pair_list[0] + "?", 5), "?"), "")
		double_list := verify_list
		for temp_itr := 0; temp_itr <= 3; temp_itr++ {
			double_list = append(double_list, verify_list...)
		}
		expand_list[temp_idx] = d12Record{expand_string, double_list}
	}
	return record_list, expand_list
}

func d12loop(in_list []string, in_verify []int) int {
	for temp_idx, temp_char := range in_list {
		if temp_char == "?" {
			dot_list := tcopy(in_list)
			dot_list[temp_idx] = "."
			hash_list := tcopy(in_list)
			hash_list[temp_idx] = "#"
			return d12loop(dot_list, in_verify) + d12loop(hash_list, in_verify)
		}
	}
	var test_verify []int
	var hash_count int
	for _, temp_char := range in_list {
		switch temp_char {
			case ".":
				if hash_count > 0 {
					test_verify = append(test_verify, hash_count)
					hash_count = 0
				}
			case "#": hash_count += 1
		}
	}
	if hash_count > 0 {
		test_verify = append(test_verify, hash_count)
	}
	if tequal(in_verify, test_verify) {
		return 1
	}
	return 0
}

func d12valid(in_record d12Record, in_group *sync.WaitGroup, in_chan chan int) {
	var valid_count int
	valid_count = d12loop(in_record.list, in_record.verify)
	in_chan <- valid_count
	in_group.Done()
}

func d12part1(in_clean []d12Record) int {
	var chan_group sync.WaitGroup
	chan_sum := make(chan int, len(in_clean))
	for _, temp_record := range in_clean {
		chan_group.Add(1)
		go d12valid(temp_record, &chan_group, chan_sum)
	}
	chan_group.Wait()
	close(chan_sum)
	var valid_sum int
	for temp_int := range chan_sum {
		valid_sum += temp_int
	}
	return valid_sum
}

func day12() (any, any) {
	file_string := tload("input/day12.txt")
	file_clean, file_second := d12clean(file_string)
	tuse(file_second)
	return d12part1(file_clean), 5 //, d12part1(file_second)
}
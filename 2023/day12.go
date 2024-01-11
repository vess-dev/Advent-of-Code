package main

import (
	"strings"
	"sync"
)

type d12Record struct {
	list []string
	verify []int
}
type d12Index struct {
	index int
	left int
}
type d12Map = map[d12Index]int

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

func d12loop(in_cache *d12Map, in_list []string, in_verify []int, in_index int) int {
	if (in_index > 0) && (in_index < len(in_list)) {
			if in_list[in_index-1] == "#" {
			return 0
		}
	}
	if len(in_verify) == 0 {
		if in_index >= len(in_list) {
			return 1
		}
		for _, temp_char := range in_list[in_index:] {
			if temp_char == "#" {
				return 0
			}
		}
		return 1
	}

	var find_index int
	L1: for find_index = in_index; true; find_index++ {
		if find_index >= len(in_list) {
			return 0
		}
		switch in_list[find_index] {
			case "#": break L1
			case "?": break L1
		}
	}
	var hash_count int
	L2: for _, temp_char := range in_list[find_index:] {
		switch temp_char {
			case ".": break L2
			default: hash_count += 1
		}
	}
	var result_sum int
	if hash_count >= in_verify[0] {
		result_sum += d12loop(in_cache, in_list, in_verify[1:], find_index + in_verify[0] + 1)
	}
	if in_list[find_index] == "?" {
		result_sum += d12loop(in_cache, in_list, in_verify, find_index + 1)
	}
	return result_sum
}

func d12valid(in_record d12Record, in_group *sync.WaitGroup, in_chan chan int) {
	var valid_count int
	cache_map := make(d12Map)
	valid_count = d12loop(&cache_map, in_record.list, in_record.verify, 0)
	in_chan <- valid_count
	in_group.Done()
}

func d12part1(in_clean []d12Record) int {
	var chan_group sync.WaitGroup
	chan_sum := make(chan int, len(in_clean))
	for _, temp_record := range in_clean {
		chan_group.Add(1)
		d12valid(temp_record, &chan_group, chan_sum)
		//break
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
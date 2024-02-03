package main

import (
	"strings"
	"sync"
	"time"
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
			//double_list = append(double_list, verify_list...)
		}
		expand_list[temp_idx] = d12Record{expand_string, double_list}
	}
	return record_list, expand_list
}

func d12check(in_list []string, in_start int, in_end int) bool {
	target_idx := in_start + in_end
	if target_idx <= len(in_list) {
		if target_idx < len(in_list) {
			if in_list[target_idx] == "#" {
				return false
			}
		}
		for temp_idx := in_start; temp_idx < target_idx; temp_idx++ {
			if in_list[temp_idx] == "." {
				return false
			}
		}
		return true
	}
	return false
}

func d12loop(in_cache *d12Map, in_list []string, in_verify []int, in_index int) int {
	in_verify = tcopy(in_verify)
	
	if in_index >= len(in_list) {
		if len(in_verify) == 0 {
			return 1
		}
		return 0
	}
	if len(in_verify) == 0 {
		for _, temp_char := range in_list[in_index:] {
			if temp_char == "#" {
				return 0
			}
		}
		return 1
	}
	var final_sum int
	switch in_list[in_index] {
	case ".":
		final_sum += d12loop(in_cache, in_list, in_verify, in_index+1)
	case "#":
		if d12check(in_list, in_index, in_verify[0]) {
			valid_offset := in_index + in_verify[0] + 1
			in_verify = tdrop(in_verify, 0)
			final_sum += d12loop(in_cache, in_list, in_verify, valid_offset)
		}
	case "?":
		final_sum += d12loop(in_cache, in_list, in_verify, in_index+1)
		if d12check(in_list, in_index, in_verify[0]) {
			valid_offset := in_index + in_verify[0] + 1
			in_verify = tdrop(in_verify, 0)
			final_sum += d12loop(in_cache, in_list, in_verify, valid_offset)
		}
	}
	return final_sum
}

func d12valid(in_record d12Record, in_group *sync.WaitGroup, in_chan chan int) {
	cache_map := make(d12Map)
	in_chan <- d12loop(&cache_map, in_record.list, in_record.verify, 0)
	in_group.Done()
}

func d12part1(in_clean []d12Record) int {
	var chan_group sync.WaitGroup
	chan_sum := make(chan int, len(in_clean))
	time_start := time.Now()
	for _, temp_record := range in_clean {
		chan_group.Add(1)
		d12valid(temp_record, &chan_group, chan_sum)
	}
	chan_group.Wait()
	close(chan_sum)
	time_since := time.Since(time_start)
	tline(time_since.Seconds())
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
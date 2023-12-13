package main

import (
	"fmt"
	"strings"
	"sync"
)

type d12Record struct {
	list string
	qcount int
	hcount int
	vcount int
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
		count_q := strings.Count(pair_list[0], "?")
		count_h := strings.Count(pair_list[0], "#")
		count_v := tsum(verify_list)
		record_list[temp_idx] = d12Record{pair_list[0], count_q, count_h, count_v, verify_list}
		expand_string := strings.TrimRight(strings.Repeat(pair_list[0] + "?", 5), "?")
		double_list := verify_list
		for temp_itr := 0; temp_itr <= 3; temp_itr++ {
			double_list = append(double_list, verify_list...)
		}
		expand_list[temp_idx] = d12Record{expand_string, (count_q * 5) + 4, count_h * 5, count_v * 5, double_list}
	}
	return record_list, expand_list
}

func d12stitch(in_string string, in_pattern []string) []string {
	string_new := make([]string, len(in_string))
	string_split := strings.Split(in_string, "")
	var ptr_pattern int
	for temp_idx, temp_char := range string_split {
		if temp_char == "?" {
			switch in_pattern[ptr_pattern] {
				case "0": string_new[temp_idx] = "."
				case "1": string_new[temp_idx] = "#"
			}	
			ptr_pattern += 1
		} else {
			string_new[temp_idx] = temp_char
		}
	}
	return string_new
}

func d12verify(in_map *map[string]bool, in_slice []string, in_verify []int) bool {
	var broke_count int
	var verify_ptr int
	var toggle_eat bool
	var toggle_break bool
	for temp_idx, temp_char := range in_slice {
		map_check := strings.Join(in_slice[temp_idx+1:], "") + fmt.Sprint(broke_count) + fmt.Sprint(verify_ptr) + fmt.Sprint(toggle_eat) + fmt.Sprint(toggle_break)
		if temp_bool, temp_check := (*in_map)[map_check]; temp_check {
			return temp_bool
		}
		switch temp_char {
			case ".":
				if toggle_eat {
					(*in_map)[map_check] = false
					return false
				}
				toggle_break = false
			case "#":
				if toggle_break {
					(*in_map)[map_check] = false
					return false
				}
				broke_count += 1
				toggle_eat = true
				if broke_count == in_verify[verify_ptr] {
					broke_count = 0
					verify_ptr += 1
					toggle_eat = false
					toggle_break = true
					if verify_ptr == len(in_verify) {
						for _, temp_char := range in_slice[temp_idx+1:] {
							if temp_char == "#" {
								(*in_map)[map_check] = false
								return false
							}
						}
						(*in_map)[map_check] = true
						return true
					}
				}
		}
	}
	return true
}

func d12valid(in_record d12Record, in_group *sync.WaitGroup, in_chan chan int) {
	var valid_count int
	bin_max := tpow(2, in_record.qcount) - 1
	mem_map := make(map[string]bool)
	for temp_itr := 0; temp_itr <= bin_max; temp_itr++ {
		if (tones(temp_itr) + in_record.hcount) == in_record.vcount {
			slice_bin := tbin(temp_itr, in_record.qcount)
			record_test := d12stitch(in_record.list, slice_bin)
			if d12verify(&mem_map, record_test, in_record.verify) {
				valid_count += 1
			}
		}
	}
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
	return d12part1(file_clean), 5//, d12part1(file_second)
}
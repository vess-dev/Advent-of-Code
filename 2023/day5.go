package main

import (
	"math"
	"sort"
	"strings"
)

type d5Range struct {
	min int
	max int
	offset int
}

func d5clean(in_raw string) ([]int, [][]d5Range) {
	string_list := strings.Split(in_raw, "\n\n")
	split_list := make([][]string, len(string_list))
	for temp_idx, temp_text := range string_list {
		split_list[temp_idx] = strings.Split(temp_text, "\n")
	}
	split_list[0] = strings.Split(split_list[0][0], ": ")
	ret_input := tcast(strings.Split(split_list[0][1], " "))
	final_list := make([][]d5Range, len(split_list[1:]))
	for temp_idx1, temp_group := range split_list[1:] {
		range_list := make([]d5Range, len(temp_group[1:]))
		for temp_idx2, temp_map := range temp_group[1:] {
			int_map := tcast(strings.Split(temp_map, " "))
			new_range := d5Range{int_map[1], int_map[1] + int_map[2], int_map[0] - int_map[1]}
			range_list[temp_idx2] = new_range
		}
		sort.Slice(range_list, func(in_x int, in_y int) bool {
			return range_list[in_x].min < range_list[in_y].min
		})
		final_list[temp_idx1] = range_list
	}
	return ret_input, final_list
}

func d5map(in_input []int, in_set []d5Range) []int {
	ret_map := tcopy(in_input)
	for _, temp_range := range in_set {
		for temp_idx, temp_int := range in_input {
			if temp_int >= temp_range.min {
				if temp_int < temp_range.max {
					ret_map[temp_idx] = temp_int + temp_range.offset
				}
			}
		}
	}
	return ret_map
}

func d5part1(in_input []int, in_ranges [][]d5Range) int {
	next_map := tcopy(in_input)
	for _, temp_set := range in_ranges {
		next_map = d5map(next_map, temp_set)
	}
	sort.Ints(next_map)
	return next_map[0]
}

func d5shake(in_min int, in_max int, in_ranges [][]d5Range) (int, int, int) {
	range_dig := tcountdigit(in_max - in_min) - 2
	range_step := tpow(10, range_dig)
	min_val := math.MaxInt
	new_min, new_max := in_min, in_max
	for temp_itr := in_min; temp_itr <= in_max; temp_itr += range_step {
		check_int := temp_itr
		for _, temp_set := range in_ranges {
			check_int = d5map([]int{check_int}, temp_set)[0]
		}
		if check_int < min_val {
			min_val = check_int
			new_min, new_max = temp_itr - range_step, temp_itr + range_step
		}
	}
	return new_min, new_max, min_val
}

func d5part2(in_input []int, in_ranges [][]d5Range) int {
	check_map := tcopy(in_input)
	min_val := math.MaxInt
	for temp_itr := 0; temp_itr <= len(in_input)-1; temp_itr += 2 {
		range_min, range_max := check_map[temp_itr], check_map[temp_itr] + check_map[temp_itr+1]
		var check_min int
		for true {
			range_min, range_max, check_min = d5shake(range_min, range_max, in_ranges)
			if check_min < min_val {
				min_val = check_min
			}
			if (range_max - range_min) < 10 {
				break
			}
		}
	}
	return min_val
}

func day5() (any, any) {
	file_string := tload("input/day5.txt")
	file_input, file_ranges := d5clean(file_string)
	return d5part1(file_input, file_ranges), d5part2(file_input, file_ranges)
}
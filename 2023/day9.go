package main

import (
	"strings"
)

func d9clean(in_raw string) [][]int {
	string_list := strings.Split(in_raw, "\n")
	final_list := make([][]int, len(string_list))
	for temp_idx, temp_list := range string_list {
		int_list := tcast(strings.Split(temp_list, " "))
		final_list[temp_idx] = int_list
	}
	return final_list
}

func d9diff(in_slice []int) []int {
	ret_slice := make([]int, len(in_slice) - 1)
	for temp_idx, temp_int := range in_slice[1:] {
		ret_slice[temp_idx] = temp_int - in_slice[temp_idx]
	}
	return ret_slice
}

func d9dig(in_slice []int, in_toggle bool) int {
	var ret_val int
	if !in_toggle {
		ret_val = in_slice[len(in_slice)-1]
	} else {
		ret_val = in_slice[0]
	}
	if !tsame(in_slice) {
		diff_slice := d9diff(in_slice)
		if !in_toggle {
			ret_val += d9dig(diff_slice, in_toggle)
		} else {
			ret_val -= d9dig(diff_slice, in_toggle)
		}
	}
	return ret_val
}

func d9part1(in_clean [][]int, in_toggle bool) int {
	var final_score int
	for _, temp_slice := range in_clean {
		final_score += d9dig(temp_slice, in_toggle)
	}
	return final_score
}

func day9() (any, any) {
	file_string := tload("input/day9.txt")
	file_clean := d9clean(file_string)
	return d9part1(file_clean, false), d9part1(file_clean, true)
}
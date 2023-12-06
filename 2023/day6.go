package main

import (
	"strings"
)

func d6clean(in_raw string) [][]int {
	string_clean := in_raw
	for strings.Contains(string_clean, "  ") {
		string_clean = strings.Replace(string_clean, "  ", " ", -1)
	}
	string_split := strings.Split(string_clean, "\n")
	string_split[0] = strings.Split(string_split[0], ": ")[1]
	string_split[1] = strings.Split(string_split[1], ": ")[1]
	int_list := make([][]int, 2)
	int_list[0] = tcast(strings.Split(string_split[0], " "))
	int_list[1] = tcast(strings.Split(string_split[1], " "))
	return int_list
}

func d6race(in_time int, in_goal int) int {
	var win_count int
	for temp_itr := 1; temp_itr < in_time; temp_itr++ {
		if (temp_itr * (in_time - temp_itr)) > in_goal {
			win_count += 1
		}
	}
	return win_count
}

func d6part1(in_clean [][]int) int {
	record_count := 1
	for temp_itr := 0; temp_itr < len(in_clean[0]); temp_itr++ {
		record_count *= d6race(in_clean[0][temp_itr], in_clean[1][temp_itr])
	}
	return record_count
}

func d6part2(in_clean [][]int) int {
	var_time := tconcatgroup(in_clean[0])
	var_goal := tconcatgroup(in_clean[1])
	return d6race(var_time, var_goal)
}

func day6() (any, any) {
	file_string := tload("input/day6.txt")
	file_clean := d6clean(file_string)
	return d6part1(file_clean), d6part2(file_clean)
}
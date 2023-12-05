package main

import (
	"strings"
)

type d5Range struct {

}

func d5clean(in_raw string) any {
	string_list := strings.Split(in_raw, "\n\n")
	split_list := make([][]string, len(string_list))
	for temp_idx, temp_text := range string_list {
		split_list[temp_idx] = strings.Split(temp_text, "\n")
	}
	split_list[0] = strings.Split(split_list[0][0], ": ")
	for temp_idx, temp_line := range split_list {
		split_list[temp_idx] = tdrop(temp_line, 0)
	}
	ret_input := tcast(strings.Split(split_list[0][0], " "))
	split_list = tdrop(split_list, 0)

	tprint(split_list)
	tuse(ret_input)
	return 5
}

func d5part1(in_clean any) any {
	return in_clean
}

func d5part2(in_clean any) any {
	return in_clean
}

func day5() (any, any) {
	file_string := tload("input/day5.txt")
	file_clean := d5clean(file_string)
	return d5part1(file_clean), d5part2(file_clean)
}
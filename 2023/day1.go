package main

import (
	"os"
	"strconv"
	"strings"
)

func d1clean(in_raw string) []int {
	string_list := strings.Split(in_raw, "\n")
	var int_list []int
	for _, itr_string := range string_list {
		int_data, int_error := strconv.Atoi(itr_string)
		check(int_error)
		int_list = append(int_list, int_data)
	}
	return int_list
}

func d1part1(in_clean []int) int {
	for _, itr_x := range in_clean {
		for _, itr_y := range in_clean {
			if itr_x + itr_y == 2020 {
				return itr_x * itr_y
			}
		}
	}
	return 0
}

func d1part2(in_clean []int) int {
	for _, itr_x := range in_clean {
		for _, itr_y := range in_clean {
			for _, itr_z := range in_clean {
				if itr_x + itr_y + itr_z == 2020 {
					return itr_x * itr_y * itr_z
				}
			}
		}
	}
	return 0
}

func day1() (any, any) {
	file_data, file_error := os.ReadFile("input/day1.txt")
	check(file_error)
	file_string := string(file_data)
	file_clean := d1clean(file_string)
	return d1part1(file_clean), d1part2(file_clean)
}
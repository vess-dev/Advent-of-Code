package main

import (
	"os"
)

func d2clean(in_raw string) any {
	out_clean := in_raw 
	return out_clean
}

func d2part1(in_clean any) any {
	return in_clean
}

func d2part2(in_clean any) any {
	return in_clean
}

func day2() (any, any) {
	file_data, file_error := os.ReadFile("input/day2.txt")
	check(file_error)
	file_string := string(file_data)
	file_clean := d2clean(file_string)
	return d2part1(file_clean), d2part2(file_clean)
}
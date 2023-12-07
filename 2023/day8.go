package main

import (
	
)

func d8clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d8part1(in_clean any) any {
	return in_clean
}

func d8part2(in_clean any) any {
	return in_clean
}

func day8() (any, any) {
	file_string := tload("input/day8.txt")
	file_clean := d8clean(file_string)
	return d8part1(file_clean), d8part2(file_clean)
}
package main

import (
	
)

func d16clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d16part1(in_clean any) any {
	return in_clean
}

func d16part2(in_clean any) any {
	return in_clean
}

func day16() (any, any) {
	file_string := tload("input/day16.txt")
	file_clean := d16clean(file_string)
	return d16part1(file_clean), d16part2(file_clean)
}
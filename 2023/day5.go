package main

import (
	
)

func d5clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
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
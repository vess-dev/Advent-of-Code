package main

import (
	
)

func d3clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d3part1(in_clean any) any {
	return in_clean
}

func d3part2(in_clean any) any {
	return in_clean
}

func day3() (any, any) {
	file_string := tload("input/day3.txt")
	file_clean := d3clean(file_string)
	return d3part1(file_clean), d3part2(file_clean)
}
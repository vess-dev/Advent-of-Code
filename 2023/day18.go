package main

import (
	
)

func d18clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d18part1(in_clean any) any {
	tuse(in_clean)
	return -1
}

func d18part2(in_clean any) any {
	tuse(in_clean)
	return -1
}

func day18() (any, any) {
	file_string := tload("input/day18.txt")
	file_clean := d18clean(file_string)
	return d18part1(file_clean), d18part2(file_clean)
}
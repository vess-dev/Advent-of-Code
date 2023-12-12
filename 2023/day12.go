package main

import (
	
)

func d12clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d12part1(in_clean any) any {
	return in_clean
}

func d12part2(in_clean any) any {
	return in_clean
}

func day12() (any, any) {
	file_string := tload("input/day12.txt")
	file_clean := d12clean(file_string)
	return d12part1(file_clean), d12part2(file_clean)
}
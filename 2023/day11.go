package main

import (
	
)

func d11clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d11part1(in_clean any) any {
	return in_clean
}

func d11part2(in_clean any) any {
	return in_clean
}

func day11() (any, any) {
	file_string := tload("input/day11.txt")
	file_clean := d11clean(file_string)
	return d11part1(file_clean), d11part2(file_clean)
}
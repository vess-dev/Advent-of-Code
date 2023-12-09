package main

import (
	
)

func d10clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d10part1(in_clean any) any {
	return in_clean
}

func d10part2(in_clean any) any {
	return in_clean
}

func day10() (any, any) {
	file_string := tload("input/day10.txt")
	file_clean := d10clean(file_string)
	return d10part1(file_clean), d10part2(file_clean)
}
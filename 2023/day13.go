package main

import (
	
)

func d13clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d13part1(in_clean any) any {
	return in_clean
}

func d13part2(in_clean any) any {
	return in_clean
}

func day13() (any, any) {
	file_string := tload("input/day13.txt")
	file_clean := d13clean(file_string)
	return d13part1(file_clean), d13part2(file_clean)
}
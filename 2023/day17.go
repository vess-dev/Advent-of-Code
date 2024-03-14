package main

import (
	
)

func d17clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d17part1(in_clean any) any {
	return in_clean
}

func d17part2(in_clean any) any {
	return in_clean
}

func day17() (any, any) {
	file_string := tload("input/day17.txt")
	file_clean := d17clean(file_string)
	return d17part1(file_clean), d17part2(file_clean)
}
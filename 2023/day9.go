package main

import (
	
)

func d9clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d9part1(in_clean any) any {
	return in_clean
}

func d9part2(in_clean any) any {
	return in_clean
}

func day9() (any, any) {
	file_string := tload("input/day9.txt")
	file_clean := d9clean(file_string)
	return d9part1(file_clean), d9part2(file_clean)
}
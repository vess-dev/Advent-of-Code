package main

import (
	
)

func d14clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d14part1(in_clean any) any {
	return in_clean
}

func d14part2(in_clean any) any {
	return in_clean
}

func day14() (any, any) {
	file_string := tload("input/day14.txt")
	file_clean := d14clean(file_string)
	return d14part1(file_clean), d14part2(file_clean)
}
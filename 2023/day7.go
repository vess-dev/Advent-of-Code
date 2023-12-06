package main

import (
	
)

func d7clean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func d7part1(in_clean any) any {
	return in_clean
}

func d7part2(in_clean any) any {
	return in_clean
}

func day7() (any, any) {
	file_string := tload("input/day7.txt")
	file_clean := d7clean(file_string)
	return d7part1(file_clean), d7part2(file_clean)
}
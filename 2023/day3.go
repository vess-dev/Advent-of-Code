package main

import (
	"strconv"
	"strings"
	"unicode"
)

type d3Type interface{
	int | rune
}

func d3clean[G d3Type](in_raw string) [][]G {
	var grid_data [][]G
	list_lines := strings.Split(in_raw, "\n")
	for _, temp_line := range list_lines {
		var line_new []G
		line_curr := strings.Split(temp_line, "")
		for _, temp_char := range line_curr {
			rune_cast := []rune(temp_char)[0]
			if unicode.IsDigit(rune_cast) {
				int_data, int_error := strconv.Atoi(temp_char)
				tcheck(int_error)
				line_new = append(line_new, G(int_data))
			} else {
				line_new = append(line_new, G(rune_cast))
			}
		}
		grid_data = append(grid_data, line_new)
	}
	return grid_data
}

func d3part1[G d3Type](in_clean [][]G) int {
	return 0
}

func d3part2[G d3Type](in_clean [][]G) int {
	return 0
}

func day3[G d3Type]() (any, any) {
	file_string := tload("input/day3.txt")
	file_clean := d3clean[G](file_string)
	return d3part1(file_clean), d3part2(file_clean)
}
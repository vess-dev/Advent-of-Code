package main

import (
	"fmt"
	"strconv"
	"strings"
	"unicode"
)

var MAP_NUM = [9]string {
	"one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
}

func d1clean(in_raw string) []string {
	string_list := strings.Split(in_raw, "\n")
	return string_list
}

func d1reverse(in_string string) string {
	var string_rev string
	for _, temp_char := range in_string { 
		string_rev = string(temp_char) + string_rev 
	} 
	return string_rev
}

func d1checkmap(in_string string) string {
	string_rev := d1reverse(in_string)
	for temp_idx, temp_comp := range MAP_NUM {
		if strings.Contains(in_string, temp_comp) || strings.Contains(string_rev, temp_comp) {
			return fmt.Sprint(temp_idx + 1)
		}
	}
	return ""
}

func d1checkline(in_string string, in_toggle bool) string {
	runes_line := []rune(in_string)
	var check_string string
	for _, temp_char := range runes_line {
		if unicode.IsDigit(temp_char) {
			return string(temp_char)
		} else {
			if in_toggle {
				check_string = check_string + string(temp_char)
				temp_string := d1checkmap(check_string)
				if len(temp_string) > 0 {
					return temp_string
				}
			}
		}
	}
	return "0"
}

func d1getnum(in_string string, in_toggle bool) int {
	var string_num string
	string_num = string_num + d1checkline(in_string, in_toggle)
	string_num = string_num + d1checkline(d1reverse(in_string), in_toggle)
	int_data, int_error := strconv.Atoi(string_num)
	tcheck(int_error)
	return int_data
}

func d1part1(in_clean []string) int {
	var total_value int
	for _, temp_line := range in_clean {
		total_value += d1getnum(temp_line, false)
	}
	return total_value
}

func d1part2(in_clean []string) int {
	var total_value int
	for _, temp_line := range in_clean {
		total_value += d1getnum(temp_line, true)
	}
	return total_value
}

func day1() (any, any) {
	file_string := tload("input/day1.txt")
	file_clean := d1clean(file_string)
	return d1part1(file_clean), d1part2(file_clean)
}
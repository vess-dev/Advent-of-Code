package main

import (
	"fmt"
	"strconv"
	"strings"
)

var d1MAP_NUM = [9]string {
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
	for temp_idx, temp_comp := range d1MAP_NUM {
		if strings.Contains(in_string, temp_comp) || strings.Contains(string_rev, temp_comp) {
			return fmt.Sprint(temp_idx + 1)
		}
	}
	return ""
}

func d1checkline(in_string string, in_toggle bool) string {
	var check_string string
	line_curr := strings.Split(in_string, "")
	for _, temp_char := range line_curr {
		if tdigit(temp_char) {
			return temp_char
		} else {
			if in_toggle {
				check_string = check_string + temp_char
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

func d1parts(in_clean []string, in_toggle bool) int {
	var total_value int
	for _, temp_line := range in_clean {
		total_value += d1getnum(temp_line, in_toggle)
	}
	return total_value
}

func day1() (any, any) {
	file_string := tload("input/day1.txt")
	file_clean := d1clean(file_string)
	return d1parts(file_clean, false), d1parts(file_clean, true)
}
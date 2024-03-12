package main

import (
	"strings"
)

type d15step struct {
	data string
	label string
	toggle bool
	focus int
}

func (self *d15step) hash(in_data string) int {
	rune_list := trunes(in_data)
	var total_hash int
	for _, temp_rune := range rune_list {
		total_hash += int(temp_rune)
		total_hash *= 17
		total_hash %= 256
	}
	return total_hash
}

func d15clean(in_raw string) []d15step {
	step_list := strings.Split(in_raw, ",")
	step_out := make([]d15step, len(step_list))
	for temp_idx, temp_step := range step_list {
		var step_label string
		var step_toggle bool
		var step_focus int
		if strings.Contains(temp_step, "=") {
			step_split := strings.Split(temp_step, "=")
			step_label = step_split[0]
			step_focus = tnum(step_split[1])
		} else {
			step_label = strings.Split(temp_step, "-")[0]
			step_toggle = true
		}
		step_out[temp_idx] = d15step{
			data: temp_step,
			label: step_label,
			toggle: step_toggle,
			focus: step_focus,
		}
	}
	return step_out
}

func d15part1(in_clean []d15step) int {
	var total_hash int
	for _, temp_step := range in_clean {
		total_hash += temp_step.hash(temp_step.data)
	}
	return total_hash
}

func d15part2(in_clean []d15step) int {
	return 5
}

func day15() (any, any) {
	file_string := tload("input/day15.txt")
	file_clean := d15clean(file_string)
	return d15part1(file_clean), d15part2(file_clean)
}
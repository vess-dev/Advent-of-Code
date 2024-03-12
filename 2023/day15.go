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

type d15lens struct {
	label string
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

func d15droplens(in_box []d15lens, in_label string) []d15lens {
	new_box := tcopy(in_box)
	for temp_idx, temp_lens := range in_box {
		if temp_lens.label == in_label {
			new_box = tdrop(in_box, temp_idx)
		}
	}
	return new_box
}

func d15haslens(in_box []d15lens, in_label string) (int, bool) {
	for temp_idx, temp_lens := range in_box {
		if temp_lens.label == in_label {
			return temp_idx, true
		}
	}
	return 0, false
}

func d15power(in_boxes [][]d15lens) int {
	var total_power int
	for temp_idxb, temp_box := range in_boxes {
		for temp_idxl, temp_lens := range temp_box {
			total_power += (temp_idxb + 1) * (temp_idxl + 1) * temp_lens.focus
		}
	}
	return total_power
}

func d15part2(in_clean []d15step) int {
	box_list := make([][]d15lens, 256)
	for _, temp_step := range in_clean {
		box_idx := temp_step.hash(temp_step.label)
		if temp_step.toggle {
			box_list[box_idx] = d15droplens(box_list[box_idx], temp_step.label) 
		} else {
			if temp_idx, temp_ok := d15haslens(box_list[box_idx], temp_step.label); temp_ok {
				box_list[box_idx][temp_idx].focus = temp_step.focus
			} else {
				box_list[box_idx] = append(box_list[box_idx], d15lens{label: temp_step.label, focus: temp_step.focus})
			}
		}
	}
	return d15power(box_list)
}

func day15() (any, any) {
	file_string := tload("input/day15.txt")
	file_clean := d15clean(file_string)
	return d15part1(file_clean), d15part2(file_clean)
}
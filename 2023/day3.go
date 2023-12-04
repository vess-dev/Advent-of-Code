package main

import (
	"strconv"
	"strings"
	mapset "github.com/deckarep/golang-set/v2"
)

type d3Point struct {
	x int
	y int
}
type d3Part struct {
	pos d3Point
	num int
}
type d3Map = map[d3Point]any

var d3MAP_REL = [8][2]int {
	{-1, -1}, {0, -1}, {1, -1}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0},
}

func d3check(in_slice []string, in_posx int, in_posy int) ([]d3Point, *d3Part) {
	var ret_string string
	var ret_point []d3Point
	for temp_itr := 0; temp_itr <= 2; temp_itr++ {
		check_x := in_posx + temp_itr
		if check_x < len(in_slice) {
			check_char := in_slice[check_x]
			if tdigit(check_char) {
				ret_string += check_char
				new_point := d3Point{check_x, in_posy}
				ret_point = append(ret_point, new_point)
			} else {
				break
			}
		}
	}
	int_data, int_error := strconv.Atoi(ret_string)
	tcheck(int_error)
	anchor_point := d3Point{in_posx, in_posy}
	int_final := d3Part{anchor_point, int_data}
	return ret_point, &int_final
}

func d3clean(in_raw string) d3Map {
	grid_data := make(d3Map)
	list_lines := strings.Split(in_raw, "\n")
	for temp_y, temp_line := range list_lines {
		line_curr := strings.Split(temp_line, "")
		for temp_x, temp_char := range line_curr {
			if temp_char != "." && !tdigit(temp_char) {
				grid_data[d3Point{temp_x, temp_y}] = temp_char
			} else if temp_char != "." {
				if grid_data[d3Point{temp_x, temp_y}] == nil {
					get_points, get_ptr := d3check(line_curr, temp_x, temp_y)
					for _, temp_point := range get_points {
						grid_data[temp_point] = get_ptr
					}
				}
			}
		}
	}
	return grid_data
}

func d3part1(in_clean d3Map) int {
	var total_part int
	part_set := mapset.NewSet[*d3Part]()
	for temp_key, temp_val := range in_clean {
		if temp_check, temp_ok := temp_val.(*d3Part); temp_ok {
			if !part_set.Contains(temp_check) {
				for _, temp_rel := range d3MAP_REL {
					if _, temp_ok := in_clean[d3Point{temp_key.x + temp_rel[0], temp_key.y + temp_rel[1]}].(string); temp_ok {
						part_set.Add(temp_check)
						break
					}
				}
			}
		}
	}
	for temp_part := range part_set.Iter() {
		total_part += temp_part.num
	}
	return total_part
}

func d3part2(in_clean d3Map) int {
	var total_part int
	for temp_key, temp_val := range in_clean {
		if temp_val == "*" {
			part_set := mapset.NewSet[*d3Part]()
			for _, temp_rel := range d3MAP_REL {
				if temp_ref, temp_ok := in_clean[d3Point{temp_key.x + temp_rel[0], temp_key.y + temp_rel[1]}].(*d3Part); temp_ok {
					part_set.Add(temp_ref)
				}
			}
			if part_set.Cardinality() == 2 {
				gear_list := part_set.ToSlice()
				total_part += (gear_list[0].num * gear_list[1].num)
			}
		}
	}
	return total_part
}

func day3() (any, any) {
	file_string := tload("input/day3.txt")
	file_clean := d3clean(file_string)
	return d3part1(file_clean), d3part2(file_clean)
}
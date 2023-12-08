package main

import (
	"strings"
)

type d8Node struct {
	l string
	r string
}
type d8Gen struct {
	queue []string
	ptr int
}
type d8Map = map[string]d8Node

var d8BYTE_A = []byte("A")[0]
var d8BYTE_Z = []byte("Z")[0]

func (self *d8Gen) Next() string {
	ret_item := self.queue[self.ptr]
	self.ptr = (self.ptr + 1) % len(self.queue)
	return ret_item
}

func d8clean(in_raw string) (d8Gen, d8Map) {
	string_list := strings.Split(in_raw, "\n\n")
	dir_list := strings.Split(string_list[0], "")
	map_list := strings.Split(string_list[1], "\n")
	map_final := make(d8Map)
	for _, temp_map := range map_list {
		map_name := strings.Split(temp_map, " = ")[0]
		map_dir := strings.Split(temp_map, ", ")
		map_left := map_dir[0][len(map_dir[0])-3:]
		map_right := map_dir[1][0:3]
		map_final[map_name] = d8Node{map_left, map_right}
	}
	return d8Gen{dir_list, 0}, map_final
}

func d8part1(in_gen d8Gen, in_map d8Map) int {
	map_current := "AAA"
	map_gen := in_gen
	var map_steps int
	for true {
		map_next := map_gen.Next()
		switch map_next {
			case "L": map_current = in_map[map_current].l
			case "R": map_current = in_map[map_current].r
		}
		map_steps += 1
		if map_current == "ZZZ" {
			break
		}
	}
	return map_steps
}

func d8done(in_slice []string) bool {
	byte_z := []byte("Z")[0]
	for _, temp_string := range in_slice {
		if temp_string[2] != byte_z {
			return false
		}
	}
	return true
}

func d8part2(in_gen d8Gen, in_map d8Map) int {
	var map_current []string
	map_gen := in_gen
	for temp_map := range in_map {
		if temp_map[2] == d8BYTE_A {
			map_current = append(map_current, temp_map)
		}
	}
	map_steps := make([]int, len(map_current))
	for true {
		map_next := map_gen.Next()
		for temp_itr, temp_string := range map_current {
			if temp_string[2] != d8BYTE_Z {
				switch map_next {
					case "L": map_current[temp_itr] = in_map[temp_string].l
					case "R": map_current[temp_itr] = in_map[temp_string].r
				}
				map_steps[temp_itr] += 1
			}
		}
		if d8done(map_current) {
			break
		}
	}
	return tlcm(map_steps[0], map_steps[1], map_steps[2:]...)
}

func day8() (any, any) {
	file_string := tload("input/day8.txt")
	file_dir, file_map := d8clean(file_string)
	return d8part2(file_dir, file_map), 5
}
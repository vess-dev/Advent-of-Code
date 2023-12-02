package main

import (
	"strconv"
	"strings"
)

type d2game struct {
	red int
	green int
	blue int
}

func d2clean(in_raw string) [][]d2game {
	string_list := strings.Split(in_raw, "\n")
	var final_list [][]d2game
	for _, temp_game := range string_list {
		game_list := strings.Split(temp_game, ": ")
		for _, temp_line := range game_list[1:] {
			draw_list := strings.Split(temp_line, "; ")
			var draw_stack []d2game
			for _, temp_draw := range draw_list {
				hand_list := strings.Split(temp_draw, ", ")
				game_new := d2game{}
				for _, temp_hand := range hand_list {
					grab_list := strings.Split(temp_hand, " ")
					int_data, int_error := strconv.Atoi(grab_list[0])
					tcheck(int_error)
					switch grab_list[1] {
						case "red":
							game_new.red = int_data
						case "green":
							game_new.green = int_data
						case "blue":
							game_new.blue = int_data
					}
				}
				draw_stack = append(draw_stack, game_new)
			}
			final_list = append(final_list, draw_stack)
		}
	}
	return final_list
}

func d2part1(in_clean [][]d2game) int {
	var total_score int
	NEXTGAME:
	for temp_idx, temp_game := range in_clean {
		for _, temp_hand := range temp_game {
			if temp_hand.red > 12 || temp_hand.green > 13 || temp_hand.blue > 14 {
				continue NEXTGAME
			}
		}
		total_score += (temp_idx + 1)
	}
	return total_score
}

func d2part2(in_clean [][]d2game) int {
	var total_score int
	for _, temp_game := range in_clean {
		var rgb_min [3]int
		for _, temp_hand := range temp_game {
			if temp_hand.red > rgb_min[0] {
				rgb_min[0] = temp_hand.red
			}
			if temp_hand.green > rgb_min[1] {
				rgb_min[1] = temp_hand.green
			}
			if temp_hand.blue > rgb_min[2] {
				rgb_min[2] = temp_hand.blue
			}
		}
		total_score += rgb_min[0] * rgb_min[1] * rgb_min[2]
	}
	return total_score
}

func day2() (any, any) {
	file_string := tload("input/day2.txt")
	file_clean := d2clean(file_string)
	return d2part1(file_clean), d2part2(file_clean)
}
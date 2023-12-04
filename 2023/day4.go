package main

import (
	"math"
	"slices"
	"strings"
)

type d4Card struct {
	numwin []int
	numhave []int
}

func d4clean(in_raw string) []d4Card {
	card_clean := strings.ReplaceAll(in_raw, "  ", " ")
	card_list := strings.Split(card_clean, "\n")
	card_final := make([]d4Card, len(card_list))
	for temp_idx, card_data := range card_list {
		card_line := strings.Split(card_data, ": ")[1]
		card_pair := strings.Split(card_line, " | ")
		card_win := tcast(strings.Split(card_pair[0], " "))
		card_have := tcast(strings.Split(card_pair[1], " "))
		card_new := d4Card{card_win, card_have}
		card_final[temp_idx] = card_new
	}
	return card_final
}

func d4part1(in_clean []d4Card) int {
	var total_score int
	for _, temp_card := range in_clean {
		var card_score int
		for _, temp_num := range temp_card.numhave {
			if slices.Contains(temp_card.numwin, temp_num) {
				card_score += 1
			}
		}
		tprint(card_score)
	}
	return total_score
}

func d4part2(in_clean []d4Card) int {
	return 0
}

func day4() (any, any) {
	file_string := tload("input/day4.txt")
	file_clean := d4clean(file_string)
	return d4part1(file_clean), d4part2(file_clean)
}
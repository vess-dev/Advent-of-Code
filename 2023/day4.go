package main

import (
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

func d4match(in_card d4Card) int {
	var card_wins int
	for _, temp_num := range in_card.numhave {
		if slices.Contains(in_card.numwin, temp_num) {
			card_wins += 1
		}
	}
	return card_wins
}

func d4score(in_wins int) int {
	if in_wins > 1 {
		return tpow(2, in_wins-1)
	}
	return in_wins
}

func d4part1(in_clean []d4Card) int {
	var total_score int
	for _, temp_card := range in_clean {
		card_wins := d4match(temp_card)
		total_score += d4score(card_wins)
	}
	return total_score
}

func d4part2(in_clean []d4Card) int {
	card_count := make([]int, len(in_clean))
	var total_cards int
	for temp_idx, temp_card := range in_clean {
		card_count[temp_idx] += 1
		card_wins := d4match(temp_card)
		for temp_win := 1; temp_win <= card_count[temp_idx]; temp_win++ {
			for temp_itr := 1; temp_itr <= card_wins; temp_itr++ {
				card_count[temp_idx + temp_itr] += 1
			}
		}
		total_cards += card_count[temp_idx]
	}
	return total_cards
}

func day4() (any, any) {
	file_string := tload("input/day4.txt")
	file_clean := d4clean(file_string)
	return d4part1(file_clean), d4part2(file_clean)
}
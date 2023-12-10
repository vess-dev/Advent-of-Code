package main

import (
	"slices"
	"sort"
	"strconv"
	"strings"
)

type d7Card struct {
	hand []string
	bid int
}

var d7CARD_RANK = map[string]int{"2":1, "3":2, "4":3, "5":4, "6":5, "7":6, "8":7, "9":8, "T":9, "J":10, "Q":11, "K":12, "A":13}
var d7JOKE_RANK = map[string]int{"J":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "Q":11, "K":12, "A":13}
var d7HAND_RANK = map[int]int{11111:1, 1112:2, 122:3, 113:4, 23:5, 14:6, 5:7}

func d7clean(in_raw string) []d7Card {
	string_list := strings.Split(in_raw, "\n")
	card_list := make([]d7Card, len(string_list))
	for temp_idx, temp_pair := range string_list {
		card_data := strings.Split(temp_pair, " ")
		card_sort := strings.Split(card_data[0], "")
		int_data, int_error := strconv.Atoi(card_data[1])
		tcheck(int_error)
		card_list[temp_idx] = d7Card{card_sort, int_data}
	}
	return card_list
}

func d7rank(in_card d7Card, in_toggle bool) int {
	card_count := make(map[string]int, 5)
	for _, temp_char := range in_card.hand {
		card_count[temp_char] += 1
	}
	joker_count := card_count["J"]
	if (in_toggle && (joker_count > 0)) {
		delete(card_count, "J")
	}
	var card_counts []int
	for _, temp_val := range card_count {
		card_counts = append(card_counts, temp_val)
	}
	slices.Sort(card_counts)
	if (in_toggle && (joker_count != 5)) {
		card_counts[len(card_counts) - 1] += joker_count 
	} else if in_toggle {
		card_counts = append(card_counts, joker_count)
	}
	hand_string := tconcatdigits(card_counts)
	hand_rank := d7HAND_RANK[hand_string]
	return hand_rank
}

func d7cmp(in_x d7Card, in_y d7Card, in_toggle bool) bool {
	rank_x := d7rank(in_x, in_toggle)
	rank_y := d7rank(in_y, in_toggle)
	if rank_x < rank_y {
		return true
	} else if rank_x > rank_y {
		return false
	}
	for temp_idx := range in_x.hand {
		if in_x.hand[temp_idx] != in_y.hand[temp_idx] {
			if !in_toggle {
				return d7CARD_RANK[in_x.hand[temp_idx]] < d7CARD_RANK[in_y.hand[temp_idx]]
			} else {
				return d7JOKE_RANK[in_x.hand[temp_idx]] < d7JOKE_RANK[in_y.hand[temp_idx]]
			}
		}
	}
	return false
}

func d7crunch(in_clean []d7Card, in_toggle bool) int {
	sort.Slice(in_clean, func(in_x int, in_y int) bool {
		return d7cmp(in_clean[in_x], in_clean[in_y], in_toggle)
	})
	var temp_score int
	for temp_idx, temp_card := range in_clean {
		temp_score += (temp_card.bid * (temp_idx + 1))
	}
	return temp_score
}

func d7part1(in_clean []d7Card) int {
	return d7crunch(in_clean, false)
}

func d7part2(in_clean []d7Card) int {
	return d7crunch(in_clean, true)
}

func day7() (any, any) {
	file_string := tload("input/day7.txt")
	file_clean := d7clean(file_string)
	return d7part1(file_clean), d7part2(file_clean)
}
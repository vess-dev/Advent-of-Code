package main

import (
	"strings"	
)

type d18Order struct {
	dir string
	len int
	color string
}
type d18Point struct {
	posx int
	posy int
}
type d18Digsite struct {
	orders []d18Order
	digsite map[d18Point]bool
}

func d18clean(in_raw string) d18Digsite {
	out_digsite := d18Digsite{}
	line_split := strings.Split(in_raw, "\n")
	for _, temp_line := range line_split {
		order_split := strings.Split(temp_line, " ")
		order_new := d18Order{order_split[0], tnumf(order_split[1]), order_split[2]}
		out_digsite.orders = append(out_digsite.orders, order_new)
	}
	return out_digsite
}

func d18part1(in_clean any) any {
	tdebug(in_clean)
	return -1
}

func d18part2(in_clean any) any {
	tdebug(in_clean)
	return -1
}

func day18() (any, any) {
	file_string := tload("input/day18.txt")
	file_clean := d18clean(file_string)
	return d18part1(file_clean), d18part2(file_clean)
}
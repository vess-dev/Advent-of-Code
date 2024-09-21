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
	pointer int
	edge int
	digmap map[d18Point]bool
	diglist []d18Point
	minx int
	maxx int
	miny int
	maxy int
}
var d18REF = map[string]d18Point {
	"R": {1, 0},
	"D": {0, -1},
	"L": {-1, 0},
	"U": {0, 1},
}
var d18MAP = map[string]string {
	"0": "R",
	"1": "D",
	"2": "L",
	"3": "U",
}

func (self *d18Digsite) has(in_point d18Point) bool {
	if self.digmap[in_point] {
		return true
	}
	return false
}

func (self *d18Digsite) set(in_point d18Point) {
	self.digmap[in_point] = true
	if in_point.posx > self.maxx {
		self.maxx = in_point.posx
	}
	if in_point.posx < self.minx {
		self.minx = in_point.posx
	}
	if in_point.posy > self.maxy {
		self.maxy = in_point.posy
	}
	if in_point.posy < self.miny {
		self.miny = in_point.posy
	}
	return
}

func (self *d18Digsite) dig(in_color bool) {
	var pos_x int
	var pos_y int
	for self.pointer < len(self.orders) {
		order_current := self.orders[self.pointer]
		if in_color {
			order_current.len = thextoint(order_current.color[2:7])
			order_current.dir = d18MAP[tcharat(order_current.color, 7)]
		}
		pos_x += d18REF[order_current.dir].posx * order_current.len
		pos_y += d18REF[order_current.dir].posy * order_current.len
		self.edge += order_current.len
		point_new := d18Point{pos_x, pos_y}
		self.set(point_new)
		self.diglist = append(self.diglist, point_new)
		self.pointer += 1
	}
	return
}

func d18clean(in_raw string) d18Digsite {
	out_digsite := d18Digsite{}
	out_digsite.digmap = make(map[d18Point]bool)
	line_split := strings.Split(in_raw, "\n")
	for _, temp_line := range line_split {
		order_split := strings.Split(temp_line, " ")
		order_new := d18Order{order_split[0], tnumf(order_split[1]), order_split[2]}
		out_digsite.orders = append(out_digsite.orders, order_new)
	}
	return out_digsite
}

func d18debug(in_digsite d18Digsite) {
	for temp_y := in_digsite.miny; temp_y <= in_digsite.maxy; temp_y++ {
		for temp_x := in_digsite.minx; temp_x <= in_digsite.maxx; temp_x++ {
			point_check := d18Point{temp_x, temp_y}
			if in_digsite.has(point_check) {
				tout("#")
			} else {
				tout(".")
			}
		}
		tnln()
	}
}

func d18cross(in_pone d18Point, in_ptwo d18Point) int {
	return (in_pone.posx * in_ptwo.posy) - (in_ptwo.posx * in_pone.posy)
}

func d18area(in_points []d18Point) int {
	var dig_area int
	for temp_idx := 0; temp_idx < len(in_points)-1; temp_idx++ {
		dig_area += d18cross(in_points[temp_idx], in_points[temp_idx+1])
	}
	dig_area = tabs(dig_area / 2)
	return dig_area
}

func d18size(in_clean d18Digsite, in_color bool) int {
	in_clean.dig(in_color)
	dig_area := d18area(in_clean.diglist)
	dig_edge := (in_clean.edge / 2) + 1
	return dig_area + dig_edge
}

func d18part1(in_clean d18Digsite) int {
	return d18size(in_clean, false)
}

func d18part2(in_clean d18Digsite) int {
	return d18size(in_clean, true)
}

func day18() (any, any) {
	file_string := tload("input/day18.txt")
	file_clean := d18clean(file_string)
	return d18part1(file_clean), d18part2(file_clean)
}
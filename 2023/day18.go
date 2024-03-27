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
	diglist []d18Point
	digmap map[d18Point]bool
	digx int
	digy int
	maxx int
	minx int
	maxy int
	miny int
}
var d18REF = map[string][]int {
	"U": {0, -1},
	"R": {1, 0},
	"D": {0, 1},
	"L": {-1, 0},
}

func (self *d18Digsite) shoe() int {
	var total_space int
	point_a := self.diglist[len(self.diglist)-1]
	for _, point_b := range self.diglist {
		total_space += ((point_a.posy * point_b.posx) - (point_a.posx * point_b.posy))
		point_a = point_b
	}
	return len(self.digmap) + tabs(total_space / 2)
}

func (self *d18Digsite) set(in_x int, in_y int) {
	point_new := d18Point{in_x, in_y}
	self.digmap[point_new] = true
	if in_x > self.maxx {
		self.maxx = in_x
	}
	if in_x < self.minx {
		self.minx = in_x
	}
	if in_y > self.maxy {
		self.maxy = in_y
	}
	if in_y < self.miny {
		self.miny = in_y
	}
	return
}

func (self *d18Digsite) vertex(in_x int, in_y int) {
	point_new := d18Point{in_x, in_y}
	self.diglist = append(self.diglist, point_new)
	return
}

func (self *d18Digsite) dig() {
	for self.pointer < len(self.orders) {
		order_current := self.orders[self.pointer]
		for temp_rep := 0; temp_rep < order_current.len; temp_rep++ {
			self.digx += d18REF[order_current.dir][0]
			self.digy += d18REF[order_current.dir][1]
			self.set(self.digx, self.digy)
		}
		self.vertex(self.digx, self.digy)
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
		for temp_x := in_digsite.minx; temp_x <= in_digsite.maxx; temp_x ++ {
			point_check := d18Point{temp_x, temp_y}
			if in_digsite.digmap[point_check] {
				tout("#")
			} else {
				tout(".")
			}
		}
		tnln()
	}
}

func d18part1(in_clean d18Digsite) int {
	tline()
	tdebug(in_clean)
	tline()
	in_clean.dig()
	tline(in_clean.digmap)
	tline()
	tdebug(in_clean)
	tline()
	d18debug(in_clean)
	tline()
	tline(len(in_clean.diglist))
	tline(in_clean.shoe())
	tline()
	return -1
}

func d18part2(in_clean d18Digsite) int {
	//tdebug(in_clean)
	tuse(in_clean)
	return -1
}

func day18() (any, any) {
	file_string := tload("input/day18.txt")
	file_clean := d18clean(file_string)
	return d18part1(file_clean), d18part2(file_clean)
}
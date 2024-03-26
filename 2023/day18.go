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

func (self *d18Digsite) size() int {
	return len(self.digmap)
}

func (self *d18Digsite) wall(in_x int, in_y int) bool {
	point_check := d18Point{in_x, in_y}
	return self.digmap[point_check]
}

func (self *d18Digsite) ray(in_x int, in_y int, in_min int, in_max int, in_vert bool) (int, int) {
	var wall_before int
	var wall_after int
	var wall_edge bool
	var wall_split int
	if !in_vert {
		wall_split = in_x
	} else {
		wall_split = in_y
	}
	for temp_itr := in_min; temp_itr <= in_max; temp_itr++ {
		var wall_check bool
		if !in_vert {
			wall_check = self.wall(temp_itr, in_y)	
		} else {
			wall_check = self.wall(in_x, temp_itr)
		}
		if wall_check && !wall_edge {
			wall_edge = true
			if temp_itr < wall_split {
				wall_before += 1
			} else {
				wall_after += 1
			}
		} else if !wall_check && wall_edge {
			wall_edge = false
		}
	}
	return wall_before, wall_after
}

func (self *d18Digsite) check(in_x int, in_y int) bool {
	count_left, count_right := self.ray(in_x, in_y, self.minx, self.maxx, false)
	count_up, count_down := self.ray(in_x, in_y, self.miny, self.maxy, true)
	//tline(in_x, in_y, count_left, count_right, count_down, count_up)
	
	return true
}

func (self *d18Digsite) space() int {
	var total_space int
	for temp_y := self.miny; temp_y <= self.maxy; temp_y++ {
		for temp_x := self.minx; temp_x <= self.maxx; temp_x++ {
			if !self.wall(temp_x, temp_y) {
				if self.check(temp_x, temp_y) {
					total_space += 1
				}
			}
		}
	}
	return self.size() + total_space
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

func (self *d18Digsite) dig() {
	for self.pointer < len(self.orders) {
		order_current := self.orders[self.pointer]
		for temp_rep := 0; temp_rep < order_current.len; temp_rep++ {
			self.digx += d18REF[order_current.dir][0]
			self.digy += d18REF[order_current.dir][1]
			self.set(self.digx, self.digy)
		}
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

func d18part1(in_clean d18Digsite) int {
	tline()
	tdebug(in_clean)
	tline()
	in_clean.dig()
	tline(in_clean.digmap)
	tline()
	tdebug(in_clean)
	tline()
	tline(in_clean.size())
	tline()
	tline(in_clean.minx, in_clean.maxx, in_clean.miny, in_clean.maxy)
	//tline(in_clean.check(2, 2))
	tline(in_clean.space())
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
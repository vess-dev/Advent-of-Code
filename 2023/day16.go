package main

import (
	"strings"
	"sync"
)

type d16grid struct {
	sizew int
	sizeh int
	grid []string
	energy map[d16energy]bool
	beams []d16beam
	history map[d16history]bool
}

type d16energy struct {
	posx int
	posy int
}

type d16beam struct {
	posx int
	posy int
	dir string
}

type d16pair struct {
	v1 string
	v2 string
}

type d16history struct {
	energy d16energy
	pair d16pair
}

var d16BEAM_REF = map[d16pair]d16pair{
	d16pair{"N", "/"}: d16pair{"E", ""},
	d16pair{"E", "/"}: d16pair{"N", ""},
	d16pair{"S", "/"}: d16pair{"W", ""},
	d16pair{"W", "/"}: d16pair{"S", ""},
	d16pair{"N", "\\"}: d16pair{"W", ""},
	d16pair{"E", "\\"}: d16pair{"S", ""},
	d16pair{"S", "\\"}: d16pair{"E", ""},
	d16pair{"W", "\\"}: d16pair{"N", ""},
	d16pair{"N", "|"}: d16pair{"N", ""},
	d16pair{"E", "|"}: d16pair{"N", "S"},
	d16pair{"S", "|"}: d16pair{"S", ""},
	d16pair{"W", "|"}: d16pair{"N", "S"},
	d16pair{"N", "-"}: d16pair{"E", "W"},
	d16pair{"E", "-"}: d16pair{"E", ""},
	d16pair{"S", "-"}: d16pair{"E", "W"},
	d16pair{"W", "-"}: d16pair{"W", ""},
}

func (self *d16grid) get(in_x int, in_y int) string {
	return self.grid[in_x + (in_y * self.sizew)]
}

func (self *d16grid) update() {
	for temp_idx := range self.beams {
		bind_x, bind_y := &self.beams[temp_idx].posx, &self.beams[temp_idx].posy
		bind_dir := &self.beams[temp_idx].dir
		switch *bind_dir {
			case "N": *bind_y -= 1
			case "E": *bind_x += 1
			case "S": *bind_y += 1
			case "W": *bind_x -= 1
		}
		energy_new := d16energy{
			posx: *bind_x,
			posy: *bind_y,
		}
		if (*bind_x < 0) || (*bind_x >= self.sizew) || (*bind_y < 0) || (*bind_y >= self.sizeh) {
			*bind_dir = ""
			continue
		}
		beam_target := self.get(*bind_x, *bind_y)
		beam_key := d16pair{*bind_dir, beam_target}
		beam_history := d16history{energy_new, beam_key}
		if _, temp_ok := self.history[beam_history]; temp_ok {
			*bind_dir = ""
			continue
		}
		self.history[beam_history] = true
		self.energy[energy_new] = true
		if beam_target != "." {
			beam_value := d16BEAM_REF[beam_key]
			*bind_dir = beam_value.v1
			if beam_value.v2 != "" {
				beam_new := d16beam{*bind_x, *bind_y, beam_value.v2}
				self.beams = append(self.beams, beam_new)
			}
		}
	}
	beams_new := tcopy(self.beams)
	var beams_offset int
	for temp_idx := range self.beams {
		if self.beams[temp_idx].dir == "" {
			beams_new = tdrop(beams_new, temp_idx + beams_offset)
			beams_offset -= 1
		}
	}
	self.beams = beams_new
	return
}

func d16start(in_x int, in_y int, in_dir string) []d16beam {
	beam_start := d16beam{
		posx: in_x,
		posy: in_y,
		dir: in_dir,
	}
	return []d16beam{beam_start}
}

func d16clean(in_raw string) d16grid {
	grid_out := d16grid{}
	line_split := strings.Split(in_raw, "\n")
	grid_out.sizeh = len(line_split)
	for _, temp_line := range line_split {
		char_split := strings.Split(temp_line, "")
		grid_out.sizew = len(char_split)
		for _, temp_char := range char_split {
			grid_out.grid = append(grid_out.grid, temp_char)
		}
	}
	grid_out.history = make(map[d16history]bool)
	return grid_out
}

func d16copy(in_grid d16grid) d16grid {
	grid_copy := d16grid{}
	grid_copy.sizew = in_grid.sizew
	grid_copy.sizeh = in_grid.sizeh
	grid_copy.grid = tcopy(in_grid.grid)
	grid_copy.energy = tcopymap(in_grid.energy)
	grid_copy.beams = tcopy(in_grid.beams)
	grid_copy.history = tcopymap(in_grid.history)
	return grid_copy
}

func d16sim(in_clean d16grid, in_start []d16beam) int {
	grid_copy := d16copy(in_clean)
	grid_copy.beams = in_start
	for len(grid_copy.beams) > 0 {
		grid_copy.update()
	}
	return len(grid_copy.energy)
}

func d16nyoom(in_group *sync.WaitGroup, in_chan chan int, in_clean d16grid, in_start []d16beam) {
	grid_copy := d16copy(in_clean)
	grid_copy.beams = in_start
	for len(grid_copy.beams) > 0 {
		grid_copy.update()
	}
	in_chan <- len(grid_copy.energy)
	in_group.Done()
	return
}

func d16part1(in_clean d16grid) int {
	return d16sim(in_clean, d16start(-1, 0, "E"))
}

func d16part2(in_clean d16grid) int {
	var chan_group sync.WaitGroup
	chan_size := (in_clean.sizew * 2) + (in_clean.sizeh * 2)
	chan_energy := make(chan int, chan_size)
	for temp_idx := 0; temp_idx < in_clean.sizew; temp_idx++ {
		chan_group.Add(2)
		go d16nyoom(&chan_group, chan_energy, in_clean, d16start(temp_idx, -1, "S"))
		go d16nyoom(&chan_group, chan_energy, in_clean, d16start(temp_idx, in_clean.sizeh, "N"))

	}
	for temp_idy := 0; temp_idy < in_clean.sizeh; temp_idy++ {
		chan_group.Add(2)
		go d16nyoom(&chan_group, chan_energy, in_clean, d16start(-1, temp_idy, "E"))
		go d16nyoom(&chan_group, chan_energy, in_clean, d16start(in_clean.sizew, temp_idy, "W"))
	}
	chan_group.Wait()
	close(chan_energy)
	var max_sum int
	for temp_int := range chan_energy {
		if temp_int > max_sum {
			max_sum = temp_int
		}
	}
	return max_sum
}

func day16() (any, any) {
	file_string := tload("input/day16.txt")
	file_clean := d16clean(file_string)
	return d16part1(file_clean), d16part2(file_clean)
}
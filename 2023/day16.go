package main

import (
	"strings"
)

type d16grid struct {
	sizew int
	sizeh int
	grid []string
	energy map[d16energy]bool
	beams []d16beam
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

func (self *d16grid) set(in_x int, in_y int) {
	self.grid[in_x + (in_y * self.sizew)] = "#"
	return 
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
		if (*bind_x < 0) || (*bind_x >= self.sizew) || (*bind_y < 0) || (*bind_y >= self.sizeh) {
			*bind_dir = ""
			continue
		}
		energy_new := d16energy{
			posx: *bind_x,
			posy: *bind_y,
		}
		self.energy[energy_new] = true
		beam_target := self.get(*bind_x, *bind_y)
		if beam_target != "." {
			beam_key := d16pair{*bind_dir, beam_target}
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
	beam_start := d16beam{
		posx: -1,
		posy: 0,
		dir: "E",
	}
	grid_out.beams = []d16beam{beam_start}
	return grid_out
}

func d16copy(in_grid d16grid) d16grid {
	grid_copy := d16grid{}
	grid_copy.sizew = in_grid.sizew
	grid_copy.sizeh = in_grid.sizeh
	grid_copy.grid = tcopy(in_grid.grid)
	grid_copy.energy = tcopymap(in_grid.energy)
	grid_copy.beams = tcopy(in_grid.beams)
	return grid_copy
}

func d16debug(in_grid d16grid) {
	for temp_key, _ := range in_grid.energy {
		in_grid.set(temp_key.posx, temp_key.posy)
	}
	for temp_idy := 0; temp_idy < in_grid.sizeh; temp_idy++ {
		out_string := ""
		for temp_idx := 0; temp_idx < in_grid.sizew; temp_idx++ {
			out_string += in_grid.get(temp_idx, temp_idy)
		}
		tprint(out_string)
	}
	return
}

func d16part1(in_clean d16grid) int {
	grid_copy := d16copy(in_clean)
	grid_energy := -1
	for grid_energy != len(grid_copy.energy) {
		tline()
		tline(grid_copy.beams)
		grid_energy = len(grid_copy.energy)
		grid_copy.update()
	}
	tline()
	tline(grid_copy.energy)
	tline(len(grid_copy.energy))
	tline()
	d16debug(grid_copy)
	return -1
}

func d16part2(in_clean d16grid) int {
	return -1
}

func day16() (any, any) {
	file_string := tload("input/day16.txt")
	file_clean := d16clean(file_string)
	return d16part1(file_clean), d16part2(file_clean)
}
package main

import (
	"strings"

	"gonum.org/v1/gonum/stat/combin"
)

type d11Planet struct {
	num int
	x int
	y int
}
type d11Map = map[int]bool

func d11clean(in_raw string) ([]d11Planet, int, int) {
	var planet_final []d11Planet
	var planet_count int
	var max_x int
	var max_y int
	string_list := strings.Split(in_raw, "\n")
	for temp_idy, temp_line := range string_list {
		planet_list := strings.Split(temp_line, "")
		for temp_idx, temp_spot := range planet_list {
			if temp_spot == "#" {
				planet_count += 1
				planet_final = append(planet_final, d11Planet{planet_count, temp_idx, temp_idy})
				if temp_idx > max_x {
					max_x = temp_idx
				}
				if temp_idy > max_y {
					max_y = temp_idy
				}
			}
		}
	}
	return planet_final, max_x, max_y
}

func d11empty(in_clean []d11Planet) (d11Map, d11Map) {
	map_x := make(d11Map)
	map_y := make(d11Map)
	for _, temp_planet := range in_clean {
		map_x[temp_planet.x] = true
		map_y[temp_planet.y] = true
	}
	return map_x, map_y
}

func d11expand(in_clean []d11Planet, in_rate int, in_mapx d11Map, in_mapy d11Map, in_maxx int, in_maxy int) []d11Planet {
	slice_new := tcopy(in_clean)
	for temp_itrx := 0; temp_itrx <= in_maxx; temp_itrx++ {
		if !in_mapx[temp_itrx] {
			for temp_idx := range in_clean {
				if in_clean[temp_idx].x > temp_itrx {
					slice_new[temp_idx].x += in_rate
				}
			}
		}
	}
	for temp_itry := 0; temp_itry <= in_maxy; temp_itry++ {
		if !in_mapy[temp_itry] {
			for temp_idx := range in_clean {
				if in_clean[temp_idx].y > temp_itry {
					slice_new[temp_idx].y += in_rate
				}
			}
		}
	}
	return slice_new
}

func d11short(in_clean []d11Planet, in_rate int, in_maxx int, in_maxy int) int {
	map_x, map_y := d11empty(in_clean)
	slice_expand := d11expand(in_clean, in_rate, map_x, map_y, in_maxx, in_maxy)
	var final_sum int
	planet_perm := combin.Combinations(len(slice_expand), 2)
	for _, planet_pair := range planet_perm {
		planet_1 := slice_expand[planet_pair[0]]
		planet_2 := slice_expand[planet_pair[1]]
		planet_dist := tsteps(planet_1.x, planet_1.y, planet_2.x, planet_2.y)
		final_sum += planet_dist
	}
	return final_sum
}

func d11part1(in_clean []d11Planet, in_maxx int, in_maxy int) int {
	return d11short(in_clean, 1, in_maxx, in_maxy)
}

func d11part2(in_clean []d11Planet, in_maxx int, in_maxy int) int {
	return d11short(in_clean, 999999, in_maxx, in_maxy)
}

func day11() (any, any) {
	file_string := tload("input/day11.txt")
	file_clean, file_maxx, file_maxy := d11clean(file_string)
	return d11part1(file_clean, file_maxx, file_maxy), d11part2(file_clean, file_maxx, file_maxy)
}
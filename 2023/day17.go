package main

import (
	"errors"
	"strings"

	"github.com/RyanCarrier/dijkstra"
)

type d17Grid struct {
	sizew int
	sizeh int
	grid []int
}
var d17VALID = map[string][]string{
	"A": {"N", "E", "S", "W"},
	"N": {"E", "W"},
	"E": {"N", "S"},
	"S": {"E", "W"},
	"W": {"N", "S"},
}
var d17MODIF = map[string][]int{
	"N": {0, -1},
	"E": {1, 0},
	"S": {0, 1},
	"W": {-1, 0},
}

func (self *d17Grid) get(in_x int, in_y int) int {
	return self.grid[in_x + (in_y * self.sizew)]
}

func d17clean(in_raw string) d17Grid {
	grid_out := d17Grid{}
	line_split := strings.Split(in_raw, "\n")
	grid_out.sizeh = len(line_split)
	for _, temp_line := range line_split {
		char_split := strings.Split(temp_line, "")
		grid_out.sizew = len(char_split)
		for _, temp_char := range char_split {
			char_cast := tnum(temp_char)
			grid_out.grid = append(grid_out.grid, char_cast)
		}
	}
	return grid_out
}

func d17addnode(in_graph *dijkstra.Graph, in_x int, in_y int, in_dir string) (int, error) {
	node_list := []string{tsnum(in_x), tsnum(in_y), in_dir}
	node_name := strings.Join(node_list, ",")
	node_int, node_check := in_graph.GetMapping(node_name)
	if node_check != nil {
		return in_graph.AddMappedVertex(node_name), errors.New("New")
	}
	return node_int, nil
}

func d17build(in_graph *dijkstra.Graph, in_grid d17Grid, in_x int, in_y int, in_dir string, in_start int, in_range int) {
	node_new, _ := d17addnode(in_graph, in_x, in_y, in_dir)
	for _, temp_ref := range d17VALID[in_dir] {
		mod_ref := d17MODIF[temp_ref]
		var node_cost int64
		for temp_mod := 1; temp_mod <= in_range; temp_mod++ {
			new_x := in_x + (mod_ref[0] * temp_mod) 
			new_y := in_y + (mod_ref[1] * temp_mod)
			if (new_x >= 0) && (new_y >= 0) && (new_x < in_grid.sizew) && (new_y < in_grid.sizeh) {
				node_cost += int64(in_grid.get(new_x, new_y))
				if (temp_mod >= in_start) {
					node_to, node_check := d17addnode(in_graph, new_x, new_y, temp_ref)
					if node_check != nil {
						d17build(in_graph, in_grid, new_x, new_y, temp_ref, in_start, in_range)
					}
					in_graph.AddArc(node_new, node_to, node_cost)
				}
			}
		}
	}
	return
}

func d17solve(in_clean d17Grid, in_start int, in_range int) int {
	graph_build := dijkstra.NewGraph()
	graph_start, _ := d17addnode(graph_build, 0, 0, "A")
	graph_end, _ := d17addnode(graph_build, 0, 0, "F")
	graph_endeast, _ := d17addnode(graph_build, in_clean.sizew-1, in_clean.sizeh-1, "E")
	graph_endsouth, _ := d17addnode(graph_build, in_clean.sizew-1, in_clean.sizeh-1, "S")
	graph_build.AddArc(graph_endeast, graph_end, 0)
	graph_build.AddArc(graph_endsouth, graph_end, 0)
	d17build(graph_build, in_clean, 0, 0, "A", in_start, in_range)
	path_best, _ := graph_build.Shortest(graph_start, graph_end)
	return int(path_best.Distance)
}

func d17part1(in_clean d17Grid) int {
	return d17solve(in_clean, 1, 3)
}

func d17part2(in_clean d17Grid) int {
	return d17solve(in_clean, 4, 10)
}

func day17() (any, any) {
	file_string := tload("input/day17.txt")
	file_clean := d17clean(file_string)
	return d17part1(file_clean), d17part2(file_clean)
}
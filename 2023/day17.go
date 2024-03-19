package main

import (
	"strings"

	goraph "gopkg.in/gyuho/goraph.v2"
)

type d17Grid struct {
	sizew int
	sizeh int
	grid []int
}
type d17Pair struct {
	modx int
	mody int
	dir string
}
type d17Point struct {
	posx int
	posy int
	dir string
	dist int
}
var d17REF = []d17Pair{
	{0, -1, "N"},
	{1, 0, "E"},
	{0, 1, "S"},
	{-1, 0, "W"},
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

func d17node(in_x int, in_y int, in_dir string, in_dist int) goraph.Node {
	node_list := []string{tsnum(in_x), tsnum(in_y), in_dir, tsnum(in_dist)}
	node_name := strings.Join(node_list, ",")
	return goraph.NewNode(node_name)
}

func d17local(in_graph goraph.Graph, in_grid d17Grid, in_x int, in_y int, in_dir string, in_dist int, in_range int, in_maxx int, in_maxy int) {
	node_new := d17node(in_x, in_y, in_dir, in_dist)
	in_graph.AddNode(node_new)
	for _, temp_ref := range d17REF {
		new_x := in_x + temp_ref.modx
		new_y := in_y + temp_ref.mody
		if (new_x >= 0) && (new_y >= 0) && (new_x < in_maxx) && (new_y < in_maxy) {
			node_cost := float64(in_grid.get(new_x, new_y))
			if ((in_dir == temp_ref.dir) && ((in_dist + 1) <= in_range)) {
				node_to := d17node(new_x, new_y, in_dir, in_dist + 1)
				node_check := in_graph.AddNode(node_to)
				if node_check {
					d17local(in_graph, in_grid, new_x, new_y, in_dir, in_dist + 1, in_range, in_grid.sizew, in_grid.sizeh)
				}
				in_graph.AddEdge(node_new.ID(), node_to.ID(), node_cost)
			} else if (in_dir != temp_ref.dir) {
				node_to := d17node(new_x, new_y, temp_ref.dir, 1)
				node_check := in_graph.AddNode(node_to)
				if node_check {
					d17local(in_graph, in_grid, new_x, new_y, temp_ref.dir, 1, in_range, in_grid.sizew, in_grid.sizeh)
				}
				in_graph.AddEdge(node_new.ID(), node_to.ID(), node_cost)
			}
			
			
		}
	}
	return
}

func d17part1(in_clean d17Grid) int {

	graph_build := goraph.NewGraph()
	d17local(graph_build, in_clean, 0, 0, "E", 0, 3, in_clean.sizew, in_clean.sizeh)
	graph_start := d17node(0, 0, "E", 0)
	graph_end := d17node(in_clean.sizew - 1, in_clean.sizeh - 1, "E", 1)
	_, node_cost, _ := goraph.Dijkstra(graph_build, graph_start.ID(), graph_end.ID())
	return int(node_cost[graph_end.ID()])
}

func d17part2(in_clean d17Grid) int {
	tuse(in_clean)
	return -1
}

func day17() (any, any) {
	file_string := tload("input/day17.txt")
	file_clean := d17clean(file_string)
	return d17part1(file_clean), d17part2(file_clean)
}
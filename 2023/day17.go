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
type d17Point struct {
	posx int
	posy int
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

func d17node(in_x int, in_y int) goraph.Node {
	node_name := tstring("(", in_x, ",", in_y, ")")
	return goraph.NewNode(node_name)
}

func d17cost(in_grid d17Grid, in_x1 int, in_y1 int, in_x2 int, in_y2 int) int {
	diff_x := tsign(in_x2 - in_x1)
	diff_y := tsign(in_y2 - in_y1)
	cost_start := in_grid.get(in_x2, in_y2)
	cost_x, cost_y := cost_start, cost_start
	if (tabs(in_y2 - in_y1) == 1) {
		for temp_idx := in_x1 + diff_x; temp_idx != in_x2 + diff_x; temp_idx += diff_x {
			cost_x += in_grid.get(temp_idx, in_x1)
		}
	}
	if (tabs(in_x2 - in_x1) == 1) {
		for temp_idy := in_y1 + diff_y; temp_idy != in_y2 + diff_y; temp_idy += diff_y {
			cost_y += in_grid.get(in_y1, temp_idy)
		}
	}
	if (cost_x == cost_start) {
		return cost_y
	}
	if (cost_y == cost_start) {
		return cost_x
	}
	return tmin(cost_x, cost_y)
}

func d17local(in_x int, in_y int, in_range int, in_maxx int, in_maxy int) []d17Point {
	point_out := []d17Point{}
	for temp_idx := (in_x - in_range); temp_idx <= (in_x + in_range); temp_idx++ {
		if (temp_idx >= 0) && (temp_idx < in_maxx) {
			for temp_idy := (in_y - in_range); temp_idy <= (in_y + in_range); temp_idy++ {
				if (temp_idy >= 0) && (temp_idy < in_maxy) {
					if ((temp_idx != in_x) && (temp_idy != in_y)) {
						if (tabs(temp_idx - in_x) == 1) || (tabs(temp_idy - in_y) == 1) {
							point_new := d17Point{temp_idx, temp_idy}
							point_out = append(point_out, point_new)
						}
					}
				}
			}
		}
	}
	return point_out
}

func d17build(in_clean d17Grid, in_range int) goraph.Graph {
	graph_out := goraph.NewGraph()
	for temp_idy := 0; temp_idy < in_clean.sizeh; temp_idy++ {
		for temp_idx := 0; temp_idx < in_clean.sizew; temp_idx++ {
			node_new := d17node(temp_idx, temp_idy)
			graph_out.AddNode(node_new)
			local_list := d17local(temp_idx, temp_idy, in_range, in_clean.sizew, in_clean.sizeh)
			for _, temp_node := range local_list {
				edge_node := d17node(temp_node.posx, temp_node.posy)
				graph_out.AddNode(edge_node)
				edge_cost := d17cost(in_clean, temp_idx, temp_idy, temp_node.posx, temp_node.posy)
				graph_out.AddEdge(node_new.ID(), edge_node.ID(), float64(edge_cost))
			}
		}
	}
	return graph_out
}

func d17part1(in_clean d17Grid) int {
	graph_build := d17build(in_clean, 3)
	tline(graph_build)
	tline()
	graph_start := d17node(0, 0)
	graph_end := d17node(in_clean.sizew - 1, in_clean.sizeh - 1)
	node_list, node_cost, _ := goraph.Dijkstra(graph_build, graph_start.ID(), graph_end.ID())
	tuse(node_list, node_cost)
	tline(node_list, node_cost)
	total_cost := 0
	for _, temp_node := range node_list {
		tline(node_cost[temp_node])
		total_cost += int(node_cost[temp_node])
	}
	tline(total_cost)
	return -1
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
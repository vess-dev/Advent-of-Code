package main
import (

"errors"
"github.com/RyanCarrier/dijkstra"
"strings"
)

type d21Point struct {
	posx int
	posy int
	tile string
}
type d21Grid struct {
	size int
	basesize int
	start d21Point
	garden []d21Point
}
var d21DIRS = map[string][]int{
	"N": {0, -1},
	"E": {1, 0},
	"S": {0, 1},
	"W": {-1, 0},
}

func (self *d21Grid) get(in_x int, in_y int) d21Point {
	return self.garden[in_x + (in_y * self.size)]
}

func (self *d21Grid) isValid(in_x int, in_y int) bool {
	if (in_x >= 0) && (in_y >= 0) && (in_x < self.size) && (in_y < self.size) {
		return true
	}
	return false
}

func d21clean(in_raw string, in_mult int) d21Grid {
	grid_out := d21Grid{}
	grid_out.basesize = tsqrt(len(in_raw))
	if (in_mult > 1) {
		in_raw = tstring(in_raw, "\n")
	}
	mult_raw := strings.Repeat(in_raw, in_mult)
	mult_raw = strings.TrimSuffix(mult_raw, "\n")
	line_split := strings.Split(mult_raw, "\n")
	grid_out.size = len(line_split)
	grid_out.start = d21Point{grid_out.size/2, grid_out.size/2, "S"}
	for temp_y, temp_line := range line_split {
		mult_line := strings.Repeat(temp_line, in_mult)
		char_split := strings.Split(mult_line, "")
		for temp_x, temp_char := range char_split {
			point_new := d21Point{temp_x, temp_y, temp_char}
			grid_out.garden	= append(grid_out.garden, point_new)
		}
	}
	return grid_out
}

func d21addnode(in_graph *dijkstra.Graph, in_point d21Point) (int, error) {
	node_list := []string{tsnum(in_point.posx), tsnum(in_point.posy)}
	node_name := strings.Join(node_list, ",")
	node_int, node_check := in_graph.GetMapping(node_name)
	if node_check != nil {
		return in_graph.AddMappedVertex(node_name), errors.New("Error")
	}
	return node_int, nil
}

func d21build(in_graph *dijkstra.Graph, in_grid d21Grid) {
	for _, temp_point := range in_grid.garden {
		node_from := in_grid.get(temp_point.posx, temp_point.posy)
		if (node_from.tile != "#") {
			node_from_id, _ := d21addnode(in_graph, temp_point)
			for _, temp_dir := range d21DIRS {
				test_x, test_y := temp_dir[0] + temp_point.posx, temp_dir[1] + temp_point.posy
				if (in_grid.isValid(test_x, test_y)) {
					node_to := in_grid.get(test_x, test_y)
					if (node_to.tile != "#") {
						node_to_id, _ := d21addnode(in_graph, node_to)
						_ = in_graph.AddArc(node_from_id, node_to_id, 1)
					}
				}
			}
		}
	}
	return
}

func d21near(in_from d21Point, in_to d21Point, in_steps int) bool {
	dist_length := tdistnum(in_from.posx, in_from.posy, in_to.posx, in_to.posy)
	if (dist_length <= in_steps) {
		return true
	}
	return false
}

func d21solve(in_clean d21Grid, in_steps int) int {
	var valid_tiles int
	path_odd := toddnum(in_steps)
	graph_build := dijkstra.NewGraph()
	graph_start, _ := d21addnode(graph_build, in_clean.start)
	d21build(graph_build, in_clean)
	for _, temp_point := range in_clean.garden {
		if (temp_point != in_clean.start && temp_point.tile != "#") {
			graph_end, _ := d21addnode(graph_build, temp_point)
			if (d21near(in_clean.start, temp_point, in_steps)) {
				path_best, _ := graph_build.Shortest(graph_start, graph_end)
				path_length := int(path_best.Distance)
				if (path_length != 0 && path_length <= in_steps && path_length % 2 == path_odd) {
					valid_tiles += 1
				}
			}
		}
	}
	if (path_odd == 0 && in_steps > 1) {
		valid_tiles += 1
	}
	return valid_tiles
}

func d21part1(in_clean d21Grid) int {
	return d21solve(in_clean, 6)
}

func d21part2(in_clean d21Grid) int {
	var step_list []int
	for temp_itr := 0.5; temp_itr <= 3.5; temp_itr += 1 {
		step_count := tfloor(float64(in_clean.basesize) * temp_itr)
		tline(step_count)
		valid_count := d21solve(in_clean, step_count)
		step_list = append(step_list, valid_count)
	}
	tline(step_list)
	return -1
}

func day21() (any, any) {
	file_string := tload("input/day21.txt")
	file_clean_one := d21clean(file_string, 1)
	file_clean_two := d21clean(file_string, 7)
	return d21part1(file_clean_one), d21part2(file_clean_two)
}
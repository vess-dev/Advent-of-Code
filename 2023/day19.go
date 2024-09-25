package main

import (
	"strings"
)

type d19Flow struct {
	final bool
	part string
	operand string
	compare int
	test func (int) bool
	mapping string
}
type d19Part struct {
	parts map[string]int
}
type d19Workflow struct {
	flows map[string][]d19Flow
	parts []d19Part
}
type d19Clamp struct {
	min int
	max int
}
type d19ClampMap = map[string]d19Clamp

func d19clean(in_raw string) d19Workflow {
	var out_workflow d19Workflow
	out_workflow.flows = make(map[string][]d19Flow)
	pair_split := strings.Split(in_raw, "\n\n")
	flows_split := strings.Split(pair_split[0], "\n")
	for _, temp_flow := range flows_split {
		flow_name := tsubstring(temp_flow, "", "{")
		flow_list := []d19Flow{}
		string_remove := flow_name + "{"
		flow_clean := strings.Replace(temp_flow, string_remove, "", -1)
		flow_clean = strings.Replace(flow_clean, "}", "", -1)
		flow_split := strings.Split(flow_clean, ",")
		for _, temp_inside := range flow_split {
			flow_new := d19Flow{}
			inside_split := strings.Split(temp_inside, ":")
			switch len(inside_split) {
			case 1:
				flow_new.final = true
				flow_new.mapping = inside_split[0]
			case 2:
				flow_new.part = tcharat(inside_split[0], 0)
				flow_operand := tcharat(inside_split[0], 1)
				flow_comparator := tnum(inside_split[0][2:])
				flow_new.operand = flow_operand
				flow_new.compare = flow_comparator
				flow_new.test = func (in_int int) bool {
					switch flow_operand {
					case "<":
						if in_int < flow_comparator {
							return true
						}
					case ">":
						if in_int > flow_comparator {
							return true
						}
					}
					return false
				}
				flow_new.mapping = inside_split[1]
			}
			flow_list = append(flow_list, flow_new)
		}
		out_workflow.flows[flow_name] = flow_list
	}
	parts_split := strings.Split(pair_split[1], "\n")
	for _, temp_part := range parts_split {
		part_new := d19Part{}
		part_new.parts = make(map[string]int)
		part_new.parts["x"] = tnum(tsubstring(temp_part, "x=", ","))
		part_new.parts["m"] = tnum(tsubstring(temp_part, "m=", ","))
		part_new.parts["a"] = tnum(tsubstring(temp_part, "a=", ","))
		part_new.parts["s"] = tnum(tsubstring(temp_part, "s=", "}"))
		out_workflow.parts = append(out_workflow.parts, part_new)
	}
	return out_workflow
}

func d19debug(in_clean d19Workflow) {
	for _, temp_flow := range in_clean.flows {
		tline(temp_flow)
	}
	for _, temp_part := range in_clean.parts {
		tline(temp_part)
	}
}

func d19part1(in_clean d19Workflow) int {
	var part_ratings int
	for _, temp_part := range in_clean.parts {
		flow_current := "in"
		for flow_current != "A" && flow_current != "R" {
			flow_list := in_clean.flows[flow_current]
			for _, temp_flow := range flow_list {
				if temp_flow.final {
					flow_current = temp_flow.mapping
					break
				} else {
					if temp_flow.test(temp_part.parts[temp_flow.part]) {
						flow_current = temp_flow.mapping
						break
					}
				}
			}
		}
		if flow_current == "A" {
			part_ratings += tsummap(temp_part.parts)
		}
	}
	return part_ratings
}

func d19apply(in_clamp *d19ClampMap, in_flow *d19Flow, in_avoid bool) {
	clamp_ref := (*in_clamp)[in_flow.part]
	switch in_flow.operand {
		case "<":
			if !in_avoid {
				clamp_ref.max = in_flow.compare - 1
			} else {
				clamp_ref.min = in_flow.compare
			}
		case ">":
			if !in_avoid {
				clamp_ref.min = in_flow.compare + 1
			} else {
				clamp_ref.max = in_flow.compare
			}

	}
	(*in_clamp)[in_flow.part] = clamp_ref
}

func d19traverse(in_clean *d19Workflow, in_clamps *[]d19ClampMap, in_flows []d19Flow, in_clamp d19ClampMap) {
	for _, temp_flow := range in_flows {
		if temp_flow.mapping == "R" && temp_flow.test != nil {
			d19apply(&in_clamp, &temp_flow, true)
		} else if temp_flow.mapping == "A" && temp_flow.test != nil {
			clamp_copy := tcopymap(in_clamp)
			d19apply(&clamp_copy, &temp_flow, false)
			*in_clamps = append(*in_clamps, clamp_copy)
			d19apply(&in_clamp, &temp_flow, true)
		} else if temp_flow.test != nil {
			clamp_copy := tcopymap(in_clamp)
			d19apply(&clamp_copy, &temp_flow, false)
			d19traverse(in_clean, in_clamps, in_clean.flows[temp_flow.mapping], clamp_copy)
			d19apply(&in_clamp, &temp_flow, true)
		} else if temp_flow.mapping == "A" {
			*in_clamps = append(*in_clamps, in_clamp)
		} else {
			d19traverse(in_clean, in_clamps, in_clean.flows[temp_flow.mapping], in_clamp)
		}
	}
}

func d19sum(in_clamp d19ClampMap) int {
	clamp_sum := 1
	for temp_key := range in_clamp {
		clamp_sum *= (in_clamp[temp_key].max - in_clamp[temp_key].min + 1)
	}
	return clamp_sum
}

func d19part2(in_clean d19Workflow, in_raw string) int {
	clamp_list := []d19ClampMap{}
	clamp_map := make(d19ClampMap)
	clamp_map["x"] = d19Clamp{1, 4000}
	clamp_map["m"] = d19Clamp{1, 4000}
	clamp_map["a"] = d19Clamp{1, 4000}
	clamp_map["s"] = d19Clamp{1, 4000}
	d19traverse(&in_clean, &clamp_list, in_clean.flows["in"], clamp_map)
	var clamp_sum int
	for _, temp_clamp := range clamp_list {
		clamp_sum += d19sum(temp_clamp)
	}
	return clamp_sum
}

func day19() (any, any) {
	file_string := tload("input/day19.txt")
	file_clean := d19clean(file_string)
	return d19part1(file_clean), d19part2(file_clean, file_string)
}
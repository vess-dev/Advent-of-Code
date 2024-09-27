package main

import (
	"math"
	"slices"
	"strings"

	deep "github.com/brunoga/deep"
	deque "github.com/gammazero/deque"
)

type d20module interface {
	process(in_caller string, in_signal bool) *bool
	getLinked() *[]string
}
type d20passer struct {
	linked []string
}
type d20flipflop struct {
	state bool
	linked []string
}
type d20conjunction struct {
	size int
	memory map[string]bool
	linked []string
}
type d20message struct {
	caller string
	signal bool
	callee string
}
type d20switchboard struct {
	countlow int
	counthigh int
	messages deque.Deque[d20message]
	switches map[string]d20module
}

func (self *d20passer) process(in_caller string, in_signal bool) *bool {
	return &in_signal
}

func (self *d20passer) getLinked() *[]string {
	return &self.linked
}

func (self *d20flipflop) process(in_caller string, in_signal bool) *bool {
	if !in_signal {
		self.state = !self.state
		return &self.state
	}
	return nil
}

func (self *d20flipflop) getLinked() *[]string {
	return &self.linked
}

func (self *d20conjunction) check() bool {
	if len(self.memory) < self.size {
		return true
	}
	for _, temp_value := range self.memory {
		if !temp_value {
			return true
		}
	}
	return false
}

func (self *d20conjunction) process(in_caller string, in_signal bool) *bool {
	self.memory[in_caller] = in_signal
	self_bool := self.check()
	return &self_bool
}

func (self *d20conjunction) getLinked() *[]string {
	return &self.linked
}

func (self *d20switchboard) run(in_times int, in_watch map[string]bool) int {
	len_watch := len(in_watch)
	watch_cycles := make(map[string]int, len_watch)
	message_default := d20message{
		callee: "broadcaster",
		signal: false,
		caller: "",
	}
	for temp_itr := 0; temp_itr < in_times; temp_itr++ {
		self.messages.PushBack(message_default)
		for self.messages.Len() > 0 {
			message_next := self.messages.PopFront()
			switch_current := self.switches[message_next.callee]
			if switch_current == nil {
				continue
			}
			signal_out := switch_current.process(message_next.caller, message_next.signal)
			if signal_out != nil {
				switch_list := switch_current.getLinked()
				for _, temp_next := range *switch_list {
					message_new := d20message{
						callee: temp_next,
						signal: *signal_out,
						caller: message_next.callee,
					}
					self.messages.PushBack(message_new)
					if in_watch != nil && in_watch[message_next.callee] && *signal_out {
						if _, temp_ok := watch_cycles[message_next.callee]; !temp_ok {
							watch_cycles[message_next.callee] = temp_itr + 1
							if len_watch == len(watch_cycles) {
								watch_list := tmaptolist(watch_cycles)
								return tlcm(watch_list[0], watch_list[1], watch_list[2:]...)
							}
						}
					}
				}
				len_list := len(*switch_list)
				if *signal_out {
					self.counthigh += len_list
				} else {
					self.countlow += len_list
				}
			}
		}
	}
	return ((self.countlow + 1000) * self.counthigh)
}

func d20clean(in_raw string) d20switchboard {
	out_board := d20switchboard{}
	out_board.switches = make(map[string]d20module)
	raw_split := strings.Split(in_raw, "\n")
	for _, temp_line := range raw_split {
		line_split := strings.Split(temp_line, " -> ")
		module_linked := strings.Split(line_split[1], ", ")
		if line_split[0] == "broadcaster" {
			module_passer := d20passer{linked: module_linked}
			out_board.switches["broadcaster"] = &module_passer
		} else if tcharat(line_split[0], 0) == "%" {
			module_name := line_split[0][1:]
			module_flipflop := d20flipflop{linked: module_linked}
			out_board.switches[module_name] = &module_flipflop
		} else if tcharat(line_split[0], 0) == "&" {
			module_name := line_split[0][1:]
			module_size := strings.Count(in_raw, module_name) - 1
			module_memory := make(map[string]bool, module_size)
			module_conjunction := d20conjunction{size: module_size, memory: module_memory, linked: module_linked}
			out_board.switches[module_name] = &module_conjunction
		}
	}
	return out_board
}

func d20part1(in_clean d20switchboard) int {
	return in_clean.run(1000, nil)
}

func d20part2(in_clean d20switchboard) int {
	switch_gates := make(map[string]bool)
	var switch_gate string
	for temp_name, temp_switch := range in_clean.switches {
		if slices.Contains(*temp_switch.getLinked(), "rx") {
			switch_gate = temp_name
			break
		}
	}
	for temp_name, temp_switch := range in_clean.switches {
		if slices.Contains(*temp_switch.getLinked(), switch_gate) {
			switch_gates[temp_name] = true
		}
	}
	return in_clean.run(math.MaxInt, switch_gates)
}

func day20() (any, any) {
	file_string := tload("input/day20.txt")
	file_clean := d20clean(file_string)
	clean_copy, _ := deep.Copy(file_clean)
	return d20part1(file_clean), d20part2(clean_copy)
}
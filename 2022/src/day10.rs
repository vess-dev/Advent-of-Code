use crate::read;
use itertools::Itertools;

#[derive(Debug, Clone)]
enum Ins {
	NOOP,
	ADDX(i8),
}

#[derive(Debug)]
struct Comp {
	memory: Vec<Ins>,
	register: i32,
	cycle: u16,
	pointer: usize,
	duration: u8,
	halt: bool,
}

impl Comp {

	fn new(ins_list: Vec<Ins>) -> Comp {
		let duration_start = match ins_list[0] {
			Ins::NOOP => 1,
			Ins::ADDX(_) => 2,
		};
		return Comp {
			memory: ins_list,
			register: 1,
			cycle: 0,
			pointer: 0,
			duration: duration_start,
			halt: false,
		};
	}

	fn clock(&mut self) {
		self.cycle += 1;
		if self.duration > 0 {
			self.duration -= 1;
			return;
		}
		match self.memory[self.pointer] {
			Ins::NOOP => (),
			Ins::ADDX(temp_val) => self.register += temp_val as i32,
		}
		self.pointer += 1;
		if self.pointer >= self.memory.len() {
			self.halt = true;
			return;
		}
		self.duration = match self.memory[self.pointer] {
			Ins::NOOP => 0,
			Ins::ADDX(temp_val) => 1,
		}
	}

}

fn clean(file_data: &String) -> Vec<Ins> {
	let ins_vec = file_data.split("\n")
		.map(|temp_line| {
			let temp_split: Vec<_> = temp_line.split(" ").collect();
			match temp_split[0] {
				"noop" => Ins::NOOP,
				"addx" => Ins::ADDX(temp_split[1].parse().unwrap()),
				_ => unreachable!(),
			}
		}).collect();
	return ins_vec;
}

fn part1(data_clean: &Vec<Ins>) -> i32 {
	let mut comp_handle = Comp::new(data_clean.clone());
	let mut signal_score = 0;
	let cycle_list = [20, 60, 100, 140, 180, 220];
	while !comp_handle.halt {
		comp_handle.clock();
		if cycle_list.contains(&comp_handle.cycle) {
			println!("{} {}", comp_handle.cycle, comp_handle.register);
			signal_score += ((comp_handle.cycle as i32) * comp_handle.register);
		}
	}
	println!("{:?}", comp_handle);
	return signal_score;
}

fn part2(data_clean: &Vec<Ins>) -> () {
	return ();
}

pub fn main() -> (i32, ()) {
	let file_raw = read::as_string("day10.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
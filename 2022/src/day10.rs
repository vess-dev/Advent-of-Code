use crate::read;

#[derive(Clone)]
enum Ins {
	NOOP,
	ADDX(i8),
}

struct Comp {
	memory: Vec<Ins>,
	register: i16,
	cycle: u8,
	pointer: usize,
	duration: u8,
	halt: bool,
	display: String,
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
			cycle: 1,
			pointer: 0,
			duration: duration_start,
			halt: false,
			display: (".".repeat(40)).repeat(6),
		};
	}

	fn draw(&mut self) {
		let target_range = [self.register - 1, self.register, self.register + 1];
		if target_range.contains(&((self.cycle - 1) as i16 % 40)) {
			self.display.replace_range(((self.cycle as usize) - 1)..(self.cycle as usize), "#");
		}
	}

	fn clock(&mut self) {
		if self.halt {
			return;
		}
		if self.duration > 0 {
			self.duration -= 1;
		}
		self.draw();
		if self.duration == 0 {
			match self.memory[self.pointer] {
				Ins::NOOP => (),
				Ins::ADDX(temp_val) => self.register += temp_val as i16,
			}
			self.pointer += 1;
			if self.pointer >= self.memory.len() {
				self.halt = true;
				return;
			}
			self.duration = match self.memory[self.pointer] {
				Ins::NOOP => 1,
				Ins::ADDX(temp_val) => 2,
			};
		}
		self.cycle += 1;
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

fn part1(data_clean: &Vec<Ins>) -> u16 {
	let mut comp_handle = Comp::new(data_clean.clone());
	let mut signal_score = 0;
	let cycle_list = [20, 60, 100, 140, 180, 220];
	while !comp_handle.halt {
		comp_handle.clock();
		if cycle_list.contains(&comp_handle.cycle) {
			signal_score += ((comp_handle.cycle as u16) * comp_handle.register as u16);
		}
	}
	return signal_score;
}

fn part2(data_clean: &Vec<Ins>) -> String {
	let mut comp_handle = Comp::new(data_clean.clone());
	while comp_handle.cycle < 240 {
		comp_handle.clock()
	}
	let mut display_format = String::new();
	for temp_pair in comp_handle.display.chars().enumerate() {
		if temp_pair.0 % 40 == 0 && temp_pair.0 != 0 {
			display_format.push_str("\r\n");
		}
		display_format.push(temp_pair.1);
	}
	return display_format;
}

pub fn main() -> (u16, String) {
	let file_raw = read::as_string("day10.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
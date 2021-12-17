use crate::read;
use itertools::Itertools;

struct Display {
	preamble: Vec<Vec<char>>,
	message: Vec<Vec<char>>,
	mapping: [Vec<char>; 10],
}

impl Display {
	fn solve(&mut self) -> u16 {
		for itr_digit in &self.preamble {
			match itr_digit.len() {
				2 => self.mapping[1] = itr_digit.to_vec(),
				3 => self.mapping[7] = itr_digit.to_vec(),
				4 => self.mapping[4] = itr_digit.to_vec(),
				7 => self.mapping[8] = itr_digit.to_vec(),
				_ => (),
			}
		}
		for itr_digit in &self.preamble {
			if itr_digit.len() == 5 {
				if self.mapping[1].iter().all(|temp_side| itr_digit.contains(temp_side)) {
					self.mapping[3] = itr_digit.to_vec();
				} else if self.mapping[4].iter().filter(|temp_side| !self.mapping[1].contains(temp_side)).all(|temp_side| itr_digit.contains(temp_side)) {
					self.mapping[5] = itr_digit.to_vec();
				} else {
					self.mapping[2] = itr_digit.to_vec();
				}
			} else if itr_digit.len() == 6 {
				if !self.mapping[1].iter().all(|temp_side| itr_digit.contains(temp_side)) {
					self.mapping[6] = itr_digit.to_vec();
				} else if self.mapping[4].iter().all(|temp_side| itr_digit.contains(temp_side)) {
					self.mapping[9] = itr_digit.to_vec();
				} else {
					self.mapping[0] = itr_digit.to_vec();
				}
			}
		}
		let mut ret_num = 0;
		for itr_pair in self.message.iter().enumerate() {
			ret_num += self.mapping.iter().position(|temp_digit| temp_digit == itr_pair.1).unwrap() as u16 * (1000 / (10u16.pow(itr_pair.0 as u32))) ;
		}
		return ret_num;
	}
}

fn clean(file_data: &String) -> Vec<Display> {
	return file_data.split("\n").map(|temp_display| {
			let mut display_split = temp_display.split(" | ");
			Display {
				preamble: display_split.next().unwrap().split(" ").map(|temp_msg| temp_msg.chars().sorted().collect()).collect(),
				message: display_split.next().unwrap().split(" ").map(|temp_msg| temp_msg.chars().sorted().collect()).collect(),
				mapping: Default::default(),
			}
		}).collect();
}

fn part1(data_clean: &Vec<Display>) -> u16 {
	return data_clean.iter().map(|temp_display| temp_display.message.clone()).flatten().filter(|temp_vec| [2, 3, 4, 7].contains(&temp_vec.len())).count() as u16;
}

fn part2(data_clean: &mut Vec<Display>) -> u32 {
	return data_clean.iter_mut().map(|temp_display| temp_display.solve() as u32).sum();
}

pub fn main() -> (u16, u32) {
	let file_raw = read::as_string("day8.txt");
	let mut file_data = clean(&file_raw);
	return (part1(&file_data), part2(&mut file_data));
}
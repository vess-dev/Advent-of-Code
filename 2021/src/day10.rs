use crate::read;
use itertools::Itertools;

struct Chunk {
	data: String,
}

impl Chunk {
	fn verify(&self, flag_finish: bool) -> String {
		let mut vec_roll = Vec::with_capacity(self.data.len());
		for itr_char in self.data.chars() {
			if [')', ']', '}', '>'].contains(&itr_char) {
				let stack_last = *vec_roll.last().unwrap();
				if !flag_finish {
					if itr_char != close(stack_last) {
						return itr_char.to_string();
					} else {
						vec_roll.pop();
					}
				} else {
					if itr_char == close(stack_last) {
						vec_roll.pop();
					}
				}
			} else {
				vec_roll.push(itr_char);
			}
		}
		if !flag_finish {
			return "".to_string();
		}
		return vec_roll.iter().rev().map(|temp_char| close(*temp_char)).collect();
	}
}

fn close(char_match: char) -> char {
	match char_match {
		'(' => ')',
		'[' => ']',
		'{' => '}',
		'<' => '>',
		_ => unreachable!(),
	}
}

fn clean(file_data: &String) -> Vec<Chunk> {
	return file_data.split("\n")
		.map(|temp_line| Chunk {data: temp_line.to_string()})
		.collect();
}

fn part1(data_clean: &Vec<Chunk>) -> u32 {
	return data_clean.iter().map(|temp_chunk| temp_chunk.verify(false)).filter(|temp_result| *temp_result != "").fold(0, |temp_acc, temp_char| temp_acc + match temp_char.as_str() {
			")" => 3,
			"]" => 57,
			"}" => 1197,
			">" => 25137,
			_ => unreachable!(),
		});
}

fn part2(data_clean: &Vec<Chunk>) -> u64 {
	let vec_eval: Vec<u64> = data_clean.iter().filter(|temp_chunk| temp_chunk.verify(false) == "").map(|temp_chunk| temp_chunk.verify(true)).map(|temp_line| temp_line.chars().fold(0, |mut temp_acc, temp_char| {
		temp_acc *= 5;
		temp_acc + match temp_char {
				')' => 1,
				']' => 2,
				'}' => 3,
				'>' => 4,
				_ => unreachable!(),
			}
	})).sorted().collect();
	return vec_eval[vec_eval.len()/2];
}

pub fn main() -> (u32, u64) {
	let file_raw = read::as_string("day10.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
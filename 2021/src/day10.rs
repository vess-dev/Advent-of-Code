use crate::read;

struct Chunk {
	data: String,
}

impl Chunk {
	fn verify(&self) -> Option<char> {
		let mut vec_roll = Vec::with_capacity(self.data.len());
		for itr_char in self.data.chars() {
			if [')', ']', '}', '>'].contains(&itr_char) {
				let stack_last = *vec_roll.last().unwrap();
				if itr_char != close(stack_last) {
					return Some(itr_char);
				} else {
					vec_roll.pop();
				}
			} else {
				vec_roll.push(itr_char);
			}
		}
		return None;
	}

	fn finish(&self) -> String {
		let mut vec_roll = Vec::with_capacity(self.data.len());
		for itr_char in self.data.chars() {
			if [')', ']', '}', '>'].contains(&itr_char) {
				let stack_last = *vec_roll.last().unwrap();
				if itr_char == close(stack_last) {
					vec_roll.pop();
				}
			} else {
				vec_roll.push(itr_char);
			}
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
	let vec_eval: Vec<Option<char>> = data_clean.iter().map(|temp_chunk| temp_chunk.verify()).filter(|temp_result| *temp_result != None).collect();
	let mut score_syntax = 0;
	for itr_result in vec_eval {
		if let Some(char_type) = itr_result {
			score_syntax += match char_type {
				')' => 3,
				']' => 57,
				'}' => 1197,
				'>' => 25137,
				_ => unreachable!(),
			}
		}
	}
	return score_syntax;
}

fn part2(data_clean: &Vec<Chunk>) -> u64 {
	let vec_eval: Vec<String> = data_clean.iter().filter(|temp_chunk| temp_chunk.verify() == None).map(|temp_chunk| temp_chunk.finish()).collect();
	let mut score_syntax = Vec::new();
	for itr_result in vec_eval {
		let mut score_line = 0;
		for itr_char in itr_result.chars() {
			score_line *= 5;
			score_line += match itr_char {
				')' => 1,
				']' => 2,
				'}' => 3,
				'>' => 4,
				_ => unreachable!(),
			}
		}
		score_syntax.push(score_line);
	}
	score_syntax.sort();
	return score_syntax[score_syntax.len()/2];
}

pub fn main() -> (u32, u64) {
	let file_raw = read::as_string("day10.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
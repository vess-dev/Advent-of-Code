use crate::read;

fn clean(file_data: &String) -> Vec<&str> {
	return file_data.split("\n").collect();
}

fn get_match(line_1: &str, line_2: &str) -> char {
	for itr_char in line_1.chars() {
		if line_2.contains(itr_char) {
			return itr_char;
		}
	}
	return ' ';
}

fn get_matches(line_1: &str, line_2: &str, line_3: &str) -> char {
	for itr_char in line_1.chars() {
		if line_2.contains(itr_char) && line_3.contains(itr_char) {
			return itr_char;
		}
	}
	return ' ';
}

fn part1(data_clean: &Vec<&str>) -> u16 {
	let char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	let mut char_score = 0;
	for itr_line in data_clean {
		let line_split = itr_line.split_at(itr_line.len() / 2);
		let char_match = get_match(line_split.0, line_split.1);
		char_score += char_list.chars().position(|temp_char| temp_char == char_match).unwrap() as u16 + 1;
	}
	return char_score;
}

fn part2(data_clean: &Vec<&str>) -> u16 {
	let char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	let mut char_score = 0;
	for itr_lines in data_clean.chunks(3) {
		let char_match = get_matches(itr_lines[0], itr_lines[1], itr_lines[2]);
		char_score += char_list.chars().position(|temp_char| temp_char == char_match).unwrap() as u16 + 1;
	}
	return char_score;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day3.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
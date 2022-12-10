use crate::read;
use itertools::Itertools;

fn clean(file_data: &String) -> Vec<char> {
	return file_data.chars().collect();
}

fn is_unique(char_slice: &[char]) -> bool {
	let mut char_vec: Vec<char> = char_slice.to_vec();
	let char_len = char_vec.len();
	char_vec = char_vec.into_iter().unique().collect();
	if char_vec.len() < char_len {
		return false;
	}
	return true;
}

fn part1(data_clean: &Vec<char>) -> u16 {
	let mut pos_start = 0;
	for itr_window in data_clean.windows(4) {
		pos_start += 1;
		if is_unique(itr_window) {
			return pos_start + 3;
		}
	}
	return 0;
}

fn part2(data_clean: &Vec<char>) -> u16 {
	let mut pos_start = 0;
	for itr_window in data_clean.windows(14) {
		pos_start += 1;
		if is_unique(itr_window) {
			return pos_start + 13;
		}
	}
	return 0;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day5.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
use crate::read;
use pathfinding::prelude::bfs;
use std::collections::HashMap;

const DIR_LIST: [(i64, i64); 4] = [
	(1, 0),
	(0, 1),
	(-1, 0),
	(0, -1),
];

#[derive(Clone, Copy, Eq, Hash, Ord, PartialEq, PartialOrd)]
struct Pos {
	loc: (i64, i64),
}

impl Pos {
	
	fn new(pos_loc: (i64, i64)) -> Pos {
		return Pos {
			loc: pos_loc,
		};
	}

	fn next(&self, data_clean: &HashMap<(i64, i64), char>) -> Vec<Pos> {
		let mut vec_next = Vec::new();
		let char_onrad = *data_clean.get(&self.loc).unwrap() as i64;
		for temp_dir in DIR_LIST {
			let new_x = self.loc.0 + temp_dir.0;
			let new_y = self.loc.1 + temp_dir.1;
			let new_pos = (new_x, new_y);
			if let Some(char_next) = data_clean.get(&new_pos) {
				let char_nextrad = *char_next as i64;
				if (char_nextrad - char_onrad) <= 1 {
					let pos_valid = Pos::new(new_pos);
					vec_next.push(pos_valid);
				}
			}
		}
		return vec_next;
	}

}

fn clean(file_data: &String) -> HashMap<(i64, i64), char> {
	let mut arr_data = HashMap::new();
	let mut data_fit = file_data.replace("S", "`");
	data_fit = data_fit.replace("E", "{");
	data_fit.split("\n")
		.enumerate()
		.for_each(|(temp_y, temp_row)| {
			temp_row.chars()
			.enumerate()
			.for_each(|(temp_x, temp_char)| {
				arr_data.insert((temp_x as i64, temp_y as i64), temp_char);
			})
		});
	return arr_data;
}

fn find(data_clean: &HashMap<(i64, i64), char>, target_char: &char) -> Vec<Pos> {
	let mut pos_list = Vec::new();
	for temp_item in data_clean {
		if temp_item.1 == target_char {
			let target_pos = Pos::new(*temp_item.0);
			pos_list.push(target_pos);
		}
	}
	return pos_list;
}

fn part1(data_clean: &HashMap<(i64, i64), char>) -> usize {
	let pos_start = find(data_clean, &'`')[0];
	let pos_end = find(data_clean, &'{')[0];
	let pos_minpath = bfs(&pos_start, |temp_pos| temp_pos.next(data_clean), |temp_pos| *temp_pos == pos_end);
	return pos_minpath.unwrap().len() - 1;
}

fn part2(data_clean: &HashMap<(i64, i64), char>) -> usize {
	let pos_start = find(data_clean, &'a');
	let pos_end = find(data_clean, &'{')[0];
	let mut pos_minpath = usize::MAX;
	for temp_pos in pos_start {
		let pos_testpath = bfs(&temp_pos, |temp_pos| temp_pos.next(data_clean), |temp_pos| *temp_pos == pos_end);
		if let Some(pos_check) = pos_testpath {
			if pos_check.len() < pos_minpath {
				pos_minpath = pos_check.len();
			}
		}
	}
	return pos_minpath - 1;
}

pub fn main() -> (usize, usize) {
	let file_raw = read::as_string("day12.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
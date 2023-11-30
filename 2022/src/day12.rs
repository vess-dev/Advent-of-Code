use crate::read;
use pathfinding::prelude::bfs;
use std::collections::HashMap;


const DIR_LIST: [(i64, i64); 4] = [
	(1, 0),
	(0, 1),
	(-1, 0),
	(0, -1),
];

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

fn walk(data_clean: &HashMap<(i64, i64), char>, walk_now: (i64, i64), walk_history: &Vec<(i64, i64)>, walk_distance: &mut usize) -> Option<Vec<(i64, i64)>> {
	let char_on = data_clean.get(&walk_now).unwrap();
	if char_on == &'`' {
		return Some(walk_history.clone());
	}
	let mut walk_current = walk_history.clone();
	walk_current.push(walk_now);
	if walk_current.len() > *walk_distance {
		return None;
	}
	let mut walk_short = Vec::new();
	for temp_pair in DIR_LIST {
		let new_x = walk_now.0 + temp_pair.0;
		let new_y = walk_now.1 + temp_pair.1;
		let walk_next = (new_x, new_y);
		if !walk_current.contains(&walk_next) {
			if let Some(char_next) = data_clean.get(&walk_next) {
				let char_nextrad = *char_next as i32;
				let char_onrad = *char_on as i32;
				if ((char_nextrad - char_onrad) >= -1) {
					if let Some(test_walk) = walk(data_clean, walk_next, &walk_current, walk_distance) {
						if test_walk.len() <= *walk_distance {
							*walk_distance = test_walk.len();
							walk_short = test_walk;
						}
					}
				}
			}
		}
	}
	if walk_short.len() != 0 {
		return Some(walk_short);
	}
	return None;
}

fn find(data_clean: &HashMap<(i64, i64), char>, target_char: &char) -> Option<(i64, i64)> {
	for temp_item in data_clean {
		if temp_item.1 == &'{' {
			return Some(*temp_item.0);
		}
	}
	return None;
}

fn part1(data_clean: &HashMap<(i64, i64), char>) -> () {
	let arr_start = find(data_clean, '{').unwrap();
	let mut arr_maxpath = data_clean.len();
	let arr_minpath = walk(data_clean, arr_start, &Vec::new(), &mut arr_maxpath)
		.unwrap();
	println!("{:?}", arr_minpath.len());
	return ();
}

fn part2(data_clean: &HashMap<(i64, i64), char>) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day12.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
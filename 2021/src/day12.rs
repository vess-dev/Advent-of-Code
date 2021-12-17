use crate::read;
use std::collections::HashMap;

enum Double {
	No,
	Yes,
}

fn clean(file_data: &String) -> HashMap<String, Vec<String>> {
	let mut cave_map: HashMap<String, Vec<String>> = HashMap::new();
	let vec_data: Vec<(&str, &str)> = file_data.split("\n")
		.map(|temp_line| {
			let mut line_split = temp_line.split("-");
			(line_split.next().unwrap(), line_split.next().unwrap())
		})
		.collect();
	for itr_cave in vec_data {
		let cave_start = itr_cave.0.to_string();
		let cave_end = itr_cave.1.to_string();
		if None == cave_map.get(&cave_start) {
			cave_map.insert(cave_start.clone(), Vec::new());
		}
		if None == cave_map.get(&cave_end) {
			cave_map.insert(cave_end.clone(), Vec::new());
		}
		cave_map.get_mut(&cave_start).unwrap().push(cave_end.clone());
		cave_map.get_mut(&cave_end).unwrap().push(cave_start.clone());
	}
	return cave_map;
}

fn walk(cave_map: &HashMap<String, Vec<String>>, cave_pathcount: &mut u32, cave_curr: &String, cave_walked: &Vec<&String>, cave_stage: &Double) {
	if cave_curr == &"end".to_string() {
		*cave_pathcount += 1;
		return;
	}
	let cave_to = cave_map.get(cave_curr).unwrap();
	for itr_to in cave_to {
		if itr_to == &"start".to_string() {
			continue;
		}
		if itr_to.chars().all(|temp_char| char::is_ascii_lowercase(&temp_char)) {
			if cave_walked.contains(&itr_to) {
				match cave_stage {
					&Double::No => {continue},
					&Double::Yes => {
						let mut cave_walkedcopy = cave_walked.clone();
						cave_walkedcopy.push(itr_to);
						walk(cave_map, cave_pathcount, itr_to, &mut cave_walkedcopy, &Double::No);
						continue;
					},
				}
			}
		}
		let mut cave_walkedcopy = cave_walked.clone();
		cave_walkedcopy.push(itr_to);
		walk(cave_map, cave_pathcount, itr_to, &mut cave_walkedcopy, cave_stage);
	}
}

fn part1(data_clean: &HashMap<String, Vec<String>>) -> u32 {
	let mut cave_pathcount = 0;
	let cave_start = "start".to_string();
	walk(&data_clean, &mut cave_pathcount, &cave_start, &vec![&cave_start], &Double::No);
	return cave_pathcount;
}

fn part2(data_clean: &HashMap<String, Vec<String>>) -> u32 {
	let mut cave_pathcount = 0;
	let cave_start = "start".to_string();
	walk(&data_clean, &mut cave_pathcount, &cave_start, &vec![&cave_start], &Double::Yes);
	return cave_pathcount;
}

pub fn main() -> (u32, u32) {
	let file_raw = read::as_string("day12.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
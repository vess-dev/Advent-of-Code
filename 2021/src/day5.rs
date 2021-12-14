use itertools::Itertools;
use std::collections::HashMap;

use crate::read;

fn clean(file_data: &String) -> Vec<((i16, i16), (i16, i16))> {
	let vec_points: Vec<((i16, i16), (i16, i16))> = file_data.split("\n")
		.map(|temp_line: &str| temp_line.split(" -> ")
			.map(|temp_pair: &str| temp_pair.split(",")
				.map(|temp_num| temp_num.parse::<i16>().unwrap())
				.collect_tuple().unwrap())
			.collect_tuple().unwrap())
		.collect();
	return vec_points;
}

fn between(hash_points: &mut HashMap<(i16, i16), u16>, point_1: (i16, i16), point_2: (i16, i16)) {
	let mut point_slope = (0, 0);
	point_slope.0 = if point_1.0 < point_2.0 { 1 } else if point_1.0 > point_2.0 { -1 } else { 0 };
	point_slope.1 = if point_1.1 < point_2.1 { 1 } else if point_1.1 > point_2.1 { -1 } else { 0 };
	let (mut itr_x, mut itr_y) = point_1;
	while (itr_x, itr_y) != point_2 {
		let point_touch = hash_points.entry((itr_x, itr_y)).or_insert(0);
		*point_touch += 1;
		itr_x += point_slope.0;
		itr_y += point_slope.1;
	}
	let point_touch = hash_points.entry(point_2).or_insert(0);
	*point_touch += 1;
}

fn ortho(point_1: (i16, i16), point_2: (i16, i16)) -> bool {
	if (point_1.0 == point_2.0) || (point_1.1 == point_2.1) {
		return true;
	}
	return false;
}

fn part1(data_clean: &Vec<((i16, i16), (i16, i16))>) -> usize {
	let mut hash_points: HashMap<(i16, i16), u16> = HashMap::new();
	for itr_point in data_clean.iter().filter(|temp_point| ortho(temp_point.0, temp_point.1)) {
		between(&mut hash_points, itr_point.0, itr_point.1);
	}
	return hash_points.values().into_iter().filter(|temp_num| **temp_num >= 2).count();
}

fn part2(data_clean: &Vec<((i16, i16), (i16, i16))>) -> usize {
	let mut hash_points: HashMap<(i16, i16), u16> = HashMap::new();
	for itr_point in data_clean {
		between(&mut hash_points, itr_point.0, itr_point.1);
	}
	return hash_points.values().into_iter().filter(|temp_num| **temp_num >= 2).count();
}

pub fn main() -> (usize, usize) {
	let file_raw = read::as_string("day5.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
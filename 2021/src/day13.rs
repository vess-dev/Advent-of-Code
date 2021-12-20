use crate::read;
use itertools::Itertools;
use std::collections::HashSet;

fn clean(file_data: &String) -> (HashSet<(u16, u16)>, Vec<(char, u16)>) {
	let mut vec_data = file_data.split("\n\n");
	let vec_points: HashSet<(u16, u16)> = vec_data.next().unwrap()
		.split("\n").map(|temp_point| temp_point.split(",")
			.map(|temp_num| temp_num.parse().unwrap())
			.collect_tuple().unwrap())
		.collect();
	let vec_folds: Vec<(char, u16)> = vec_data.next().unwrap()
		.split("\n").map(|temp_line| {
			let mut temp_split = temp_line.split("=");
			(temp_split.next().unwrap().chars().last().unwrap(), 
				temp_split.next().unwrap().parse().unwrap())
	})
		.collect();
	return (vec_points, vec_folds);
}

fn fold(point_set: &mut HashSet<(u16, u16)>, point_fold: &(char, u16)) {
	for itr_point in point_set.clone().iter() {
		match point_fold.0 {
			'x' => {
				if itr_point.0 > point_fold.1 {
					point_set.remove(itr_point);
					let mut point_new = itr_point.clone();
					point_new.0 -= (itr_point.0 - point_fold.1) * 2;
					point_set.insert(point_new);
				}
			},
			'y' => {
				if itr_point.1 > point_fold.1 {
					point_set.remove(itr_point);
					let mut point_new = itr_point.clone();
					point_new.1 -= (itr_point.1 - point_fold.1) * 2;
					point_set.insert(point_new);
				}
			},
			_ => unreachable!(),
		}
	}
}

fn part1(data_clean: &mut (HashSet<(u16, u16)>, Vec<(char, u16)>)) -> u16 {
	fold(&mut data_clean.0, &data_clean.1[0]);
	return data_clean.0.len() as u16;
}

fn part2(data_clean: &mut (HashSet<(u16, u16)>, Vec<(char, u16)>)) -> String {
	for itr_fold in data_clean.1.iter().skip(1) {
		fold(&mut data_clean.0, itr_fold);
	}
	let mut max_point = (0, 0);
	for itr_point in data_clean.0.iter() {
		if itr_point.0 > max_point.0 {
			max_point.0 = itr_point.0;
		}
		if itr_point.1 > max_point.1 {
			max_point.1 = itr_point.1;
		}
	}
	let mut string_full = String::new();
	for itr_y in 0..max_point.1+1 {
		let mut string_line = String::with_capacity(max_point.0.into());
		for itr_x in 0..max_point.0+1 {
			if data_clean.0.contains(&(itr_x, itr_y)) {
				string_line.push('X');
			} else {
				string_line.push(' ');
			}
		}
		string_full = format!("{}{}\n", string_full, string_line);
	}
	return string_full;
}

pub fn main() -> (u16, String) {
	let file_raw = read::as_string("day13.txt");
	let mut file_data = clean(&file_raw);
	return (part1(&mut file_data), part2(&mut file_data));
}
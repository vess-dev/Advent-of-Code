use crate::read;
use array2d::Array2D;
use std::collections::HashMap;

fn clean(file_data: &String) -> Array2D<((u16, u16), u8)> {
	let vec_data: Vec<Vec<((u16, u16), u8)>> = file_data.split("\n"
		).enumerate()
		.map(|(temp_ypos, temp_line)| temp_line
			.chars()
			.enumerate()
			.map(|(temp_xpos, temp_char)| ((temp_xpos as u16, temp_ypos as u16), temp_char
				.to_digit(10).unwrap() as u8))
				.collect())
			.collect();
	return Array2D::from_rows(&vec_data).unwrap();
}

fn sight(forest_seen: &mut HashMap<(u16, u16), bool>, forest_slice: &Vec<((u16, u16), u8)>) -> () {
	for (temp_pos, (temp_loc, _)) in forest_slice.iter().enumerate() {
		if forest_slice.iter()
			.take(temp_pos)
			.any(|(_, temp_check)| temp_check >= &forest_slice[temp_pos].1) {
				continue;
		}
		forest_seen.insert(*temp_loc, true);
	}
	return;
}

fn part1(data_clean: &Array2D<((u16, u16), u8)>) -> u16 {
	let mut forest_seen: HashMap<(u16, u16), bool> = HashMap::new();
	for temp_row in data_clean.as_rows() {
		let rev_row = temp_row.clone().into_iter().rev().collect();
		sight(&mut forest_seen, &temp_row);
		sight(&mut forest_seen, &rev_row);
	}
	for temp_col in data_clean.as_columns().iter() {
		let rev_col = temp_col.clone().into_iter().rev().collect();
		sight(&mut forest_seen, &temp_col);
		sight(&mut forest_seen, &rev_col);
	}
	return forest_seen.len() as u16;
}

fn line(forest_slice: &Vec<((u16, u16), u8)>, forest_pos: usize) -> u16 {
	let mut forest_count = 0;
	for (temp_pos, (temp_loc, _)) in forest_slice.iter()
		.enumerate()
		.take(forest_pos)
		.rev() {
			if forest_slice.iter()
				.take(temp_pos)
				.any(|(_, temp_check)| temp_check >= &forest_slice[forest_slice.len() - temp_pos - 1].1) {
					continue;
				}
			forest_count += 1;
	}
	return forest_count as u16;
}

use std::process;

fn score(forest_row: &Vec<((u16, u16), u8)>, forest_col: &Vec<((u16, u16), u8)>, forest_pos: (usize, usize)) -> u32 {
	let rev_row = forest_row.clone().into_iter().rev().collect();
	let rev_col = forest_col.clone().into_iter().rev().collect();
	println!("{:?}", forest_row);
	println!("{:?}", rev_row);
	println!("{:?}", forest_col);
	println!("{:?}", rev_col);
	println!("{:?}", forest_pos);
	let mut score_current = 1;
	score_current *= line(forest_row, forest_pos.0) as u32;
	score_current *= line(&rev_row, forest_row.len() - forest_pos.0 - 1) as u32;
	score_current *= line(forest_col, forest_pos.0) as u32;
	score_current *= line(&rev_col, forest_col.len() - forest_pos.1 - 1) as u32;
	println!("{:?}", score_current);
	println!();
	//process::exit(1);
	return score_current;
}

fn part2(data_clean: &Array2D<((u16, u16), u8)>) -> u32 {
	let forest_rows = data_clean.as_rows();
	let forest_cols = data_clean.as_columns();
	let mut score_max = 0;
	for temp_xpos in 0..data_clean.column_len() {
		for temp_ypos in 0..data_clean.row_len() {
			let score_check = score(&forest_rows[temp_ypos], &forest_cols[temp_xpos], (temp_xpos, temp_ypos));
			if score_check > score_max {
				score_max = score_check;
			}
		}
	}
	return score_max;
}

pub fn main() -> (u16, u32) {
	let file_raw = read::as_string("day8.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
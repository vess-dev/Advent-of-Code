use crate::read;
use array2d::Array2D;
use std::collections::HashSet;

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

fn sight(forest_seen: &mut HashSet<(u16, u16)>, forest_slice: &Vec<((u16, u16), u8)>) -> () {
	for (temp_pos, (temp_loc, _)) in forest_slice.iter().enumerate() {
		if forest_slice.iter()
			.take(temp_pos)
			.any(|(_, temp_check)| temp_check >= &forest_slice[temp_pos].1) {
				continue;
		}
		forest_seen.insert(*temp_loc);
	}
	return;
}

fn part1(data_clean: &Array2D<((u16, u16), u8)>) -> u16 {
	let mut forest_seen: HashSet<(u16, u16)> = HashSet::new();
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

fn tower(forest_slice: &Vec<((u16, u16), u8)>, tree_height: u8) -> u16 {
	let mut tree_count = 0;
	for (temp_pos, (_, temp_tree)) in forest_slice.iter().enumerate() {
		tree_count += 1;
		if *temp_tree >= tree_height {
			break;
		}
	}
	return tree_count;
}

fn part2(data_clean: &Array2D<((u16, u16), u8)>) -> u32 {
	let forest_rows = data_clean.as_rows();
	let forest_cols = data_clean.as_columns();
	let mut score_max = 0;
	for temp_xpos in 0..data_clean.column_len() {
		for temp_ypos in 0..data_clean.row_len() {
			let tree_height = data_clean.get(temp_ypos, temp_xpos).unwrap().1;
			let check_row = &forest_rows[temp_ypos];
			let check_col = &forest_cols[temp_xpos];
			let check_rowsize = check_row.len() - temp_xpos - 1;
			let check_colsize = check_col.len() - temp_ypos - 1;
			let check_left = check_row.clone().into_iter().take(temp_xpos).rev().collect();
			let check_right = check_row.clone().into_iter().rev().take(check_rowsize).rev().collect();
			let check_up = check_col.clone().into_iter().take(temp_ypos).rev().collect();
			let check_down = check_col.clone().into_iter().rev().take(check_colsize).rev().collect();
			let mut score_current = 1;
			score_current *= tower(&check_left, tree_height) as u32;
			score_current *= tower(&check_right, tree_height) as u32;
			score_current *= tower(&check_up, tree_height) as u32;
			score_current *= tower(&check_down, tree_height) as u32;
			if score_current > score_max {
				score_max = score_current;
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
use crate::read;
use array2d::Array2D;

fn clean(file_data: &String) -> Array2D<char> {
	let vec_rows: Vec<Vec<char>> = file_data.split("\n")
		.map(|temp_row| temp_row.chars()
			.collect())
		.collect();
	return Array2D::from_rows(&vec_rows).unwrap();
}

fn walk(data_clean: &Array2D<char>, walk_x: usize, walk_y: usize, walk_history: Vec<(usize, usize)>) -> Option<Vec<(usize, usize)>> {
	
	return None;
}

fn find(data_clean: &Array2D<char>) -> (usize, usize) {
	let arr_height = data_clean.num_rows();
	let arr_width = data_clean.num_columns();
	for temp_x in 0..arr_height {
		for temp_y in 0..arr_height {
			if data_clean.get(temp_y, temp_x) == Some(&'S') {
				return (temp_x, temp_y);
			}
		}
	}
	return (0, 0);
}

fn part1(data_clean: &Array2D<char>) -> () {
	let arr_start = find(data_clean);
	println!("{:?}", arr_start);
	return ();
}

fn part2(data_clean: &Array2D<char>) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day12.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
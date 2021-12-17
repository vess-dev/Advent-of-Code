use crate::read;
use array2d::Array2D;

fn clean(file_data: &String) -> Array2D<u8> {
	let vec_data: Vec<Vec<u8>> = file_data.split("\n")
		.map(|temp_line| temp_line.split_terminator("").skip(1)
			.map(|temp_char| temp_char.parse::<u8>().unwrap())
			.collect())
		.collect();
	return Array2D::from_rows(&vec_data);
}

fn near(array_point: (usize, usize), max_x: usize, max_y: usize) -> Vec<(usize, usize)> {
	let mut dir_viable = Vec::with_capacity(8);
	let dir_check: [(i8, i8); 8] = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)];
	for itr_check in dir_check {
		let test_x = array_point.0 as i8 + itr_check.0;
		let test_y = array_point.1 as i8 + itr_check.1;
		if (0..max_x as i8).contains(&test_x) && (0..max_y as i8).contains(&test_y) {
			dir_viable.push((usize::try_from(test_x).unwrap(), usize::try_from(test_y).unwrap()))
		}
	}
	return dir_viable;
}

fn bump(octo_array: &mut Array2D<u8>, octo_cooldown: &mut Vec<(usize, usize)>, octo_point: (usize, usize)) {
	for (itr_x, itr_y) in near(octo_point, octo_array.row_len(), octo_array.column_len()) {
		let ref mut octo_ref = octo_array[(itr_y, itr_x)];
		*octo_ref += 1;
		if *octo_ref > 9 {
			if !octo_cooldown.contains(&(itr_x, itr_y)) {
				octo_cooldown.push((itr_x, itr_y));
				bump(octo_array, octo_cooldown, (itr_x, itr_y));
			}
		}
	}
}

fn step(octo_array: &mut Array2D<u8>) -> u16 {
	let max_x = octo_array.row_len();
	let max_y = octo_array.column_len();
	let mut octo_cooldown: Vec<(usize, usize)> = Vec::new();
	for itr_x in 0..max_x {
		for itr_y in 0..max_y {
			let ref mut octo_ref = octo_array[(itr_y, itr_x)];
			*octo_ref += 1;
		}
	}
	for itr_x in 0..max_x {
		for itr_y in 0..max_y {
			if !octo_cooldown.contains(&(itr_x, itr_y)) {
				let ref mut octo_ref = octo_array[(itr_y, itr_x)];
				if *octo_ref > 9 {
					octo_cooldown.push((itr_x, itr_y));
					bump(octo_array, &mut octo_cooldown, (itr_x, itr_y));
				}
			}
		}
	}
	for itr_x in 0..max_x {
		for itr_y in 0..max_y {
			let ref mut octo_ref = octo_array[(itr_y, itr_x)];
			if *octo_ref > 9 {
				*octo_ref = 0;
			}
		}
	}
	return octo_cooldown.len() as u16;
}

fn part1(data_clean: &Array2D<u8>) -> u16 {
	let mut octo_array = data_clean.clone();
	let mut octo_flash: u16 = 0;
	for itr_step in 0..100 {
		octo_flash += step(&mut octo_array);
	}
	return octo_flash;
}

fn part2(data_clean: &Array2D<u8>) -> u16 {
	let mut octo_array = data_clean.clone();
	let mut octo_steps = 1;
	loop {
		let octo_flash = step(&mut octo_array);
		if octo_flash == (data_clean.row_len() * data_clean.column_len()) as u16 {
			return octo_steps;
		}
		octo_steps += 1
	}
	return 0;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day11.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
use crate::read;
use array2d::Array2D;

fn clean(file_data: &String) -> Array2D<i8> {
	let vec_data: Vec<Vec<i8>> = file_data.split("\n")
		.map(|temp_line| temp_line.split_terminator("").skip(1)
			.map(|temp_char| temp_char.parse::<i8>().unwrap())
			.collect())
		.collect();
	return Array2D::from_rows(&vec_data);
}

fn low(data_clean: &Array2D<i8>) -> Vec<(usize, usize, i8)> {
	let dir_check: [(i8, i8); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
	let mut vec_low = Vec::new();
	for itr_x in 0..data_clean.row_len() {
		for itr_y in 0..data_clean.column_len() {
			let num_base = data_clean.get(itr_y, itr_x).unwrap();
			let mut flag_add = true;
			for itr_check in dir_check {
				let test_x = itr_x as i8 + itr_check.0;
				let test_y = itr_y as i8 + itr_check.1;
				if (0..data_clean.row_len() as i8).contains(&test_x) && (0..data_clean.column_len() as i8).contains(&test_y) {
					let num_cmp = data_clean.get(usize::try_from(test_y).unwrap(), usize::try_from(test_x).unwrap()).unwrap();
					if num_cmp <= num_base {
						flag_add = false;
						break;
					}
				}
			}
			if flag_add {
				vec_low.push((itr_x, itr_y, *num_base));
			}
		}
	}
	return vec_low;
}

fn walk(data_clean: &Array2D<i8>, vec_walked: &mut Vec<(i8, i8)>, base_point: (usize, usize)) -> u16 {
	let dir_check: [(i8, i8); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
	let mut ret_num = 0;
	for itr_check in dir_check {
		let test_x = base_point.0 as i8 + itr_check.0;
		let test_y = base_point.1 as i8 + itr_check.1;
		if (0..data_clean.row_len() as i8).contains(&test_x) && (0..data_clean.column_len() as i8).contains(&test_y) {
			let go_x = usize::try_from(test_x).unwrap();
			let go_y = usize::try_from(test_y).unwrap();
			let num_cmp = data_clean.get(go_y, go_x).unwrap();
			if *num_cmp != 9 {
				if !vec_walked.contains(&(test_x, test_y)) {
					vec_walked.push((test_x, test_y));
					ret_num += walk(data_clean, vec_walked, (go_x, go_y));
				}
			}
		}
	}
	ret_num += 1;
	return ret_num;
}

fn part1(data_clean: &Array2D<i8>) -> u16 {
	return low(data_clean).iter().map(|temp_pair| (temp_pair.2 + 1) as u16).sum();
}

fn part2(data_clean: &Array2D<i8>) -> u32 {
	let vec_low = low(data_clean);
	let mut vec_count = Vec::new();
	for itr_low in vec_low {
		vec_count.push(walk(data_clean, &mut Vec::new(), (itr_low.0, itr_low.1)) - 1);
	}
	vec_count.sort();
	return vec_count.iter().rev().take(3).map(|temp_num| *temp_num as u32).fold(1, |temp_acc, temp_num| temp_acc * temp_num);
}

pub fn main() -> (u16, u32) {
	let file_raw = read::as_string("day9.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
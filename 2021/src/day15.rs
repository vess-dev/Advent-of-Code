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

fn walk(point_array: &Array2D<u8>, point_curr: (usize, usize), point_targ: (usize, usize), point_walked: &Vec<(usize, usize)>, tally_current: u32, tally_lowest: &mut u32) {
	if point_curr == point_targ {
		if tally_current < *tally_lowest {
			*tally_lowest = tally_current;
		}
	}
	let dir_check: [(i8, i8); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];
	for temp_check in dir_check {
		let point_new = (point_curr.0 as i8 + temp_check.0, point_curr.1 as i8 + temp_check.1);
		if (0..point_array.row_len() as i8).contains(&point_new.0) {
			if (0..point_array.column_len() as i8).contains(&point_new.1) {
				let point_cast = (usize::try_from(point_new.0).unwrap(), usize::try_from(point_new.1).unwrap());
				if !point_walked.contains(&point_cast) {
					let mut point_walkedcopy = point_walked.clone();
					point_walkedcopy.push(point_cast);
					walk(point_array, point_cast, point_targ, &point_walkedcopy, tally_current + point_array.get(point_cast.1, point_cast.0).unwrap().clone() as u32, tally_lowest);
				}
			}
		}
	}
}

fn part1(data_clean: &Array2D<u8>) -> u32 {
	let mut risk_low = u32::MAX;
	let point_targ = (data_clean.row_len() - 1, data_clean.column_len() - 1);
	walk(data_clean, (0, 0), point_targ, &vec![(0,0)], *data_clean.get(0, 0).unwrap() as u32, &mut risk_low);
	return risk_low;
}

fn part2(data_clean: &Array2D<u8>) -> () {
	return ();
}

pub fn main() -> (u32, ()) {
	let file_raw = read::as_string("day15.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
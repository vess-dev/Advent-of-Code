use crate::read;

fn clean(file_data: &String) -> Vec<i32> {
	return file_data.split(",").map(|temp_num| temp_num.parse().unwrap()).collect();
}

fn burn(pos_spot: i32) -> i32 {
	return (pos_spot.pow(2)+pos_spot)/2;
}

fn walk(data_clean: &Vec<i32>, flag_burn: bool) -> i32 {
	let mut vec_fuel: Vec<i32> = Vec::with_capacity(data_clean.len());
	let vec_min = *data_clean.iter().min().unwrap();
	let vec_max = *data_clean.iter().max().unwrap();
	for itr_spot in vec_min..=vec_max {
		if flag_burn {
			vec_fuel.push(data_clean.iter().map(|temp_num| burn(*temp_num - itr_spot)).sum());
		} else {
			vec_fuel.push(data_clean.iter().map(|temp_num| (temp_num - itr_spot).abs()).sum());
		}
	}
	return *vec_fuel.iter().min().unwrap();
}

fn part1(data_clean: &Vec<i32>) -> i32 {
	return walk(data_clean, false);
}

fn part2(data_clean: &Vec<i32>) -> i32 {
	return walk(data_clean, true);
}

pub fn main() -> (i32, i32) {
	let file_raw = read::as_string("day7.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
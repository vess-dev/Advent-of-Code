use crate::read;

fn clean(file_data: String) -> Vec<i32> {
	return file_data.split(",").map(|temp_num| temp_num.parse().unwrap()).collect();
}

fn burn(pos_start: i32, pos_goal: i32) -> i32 {
	return (1..=(pos_start - pos_goal).abs()).sum();
}

fn walk(data_clean: &Vec<i32>, flag_burn: bool) -> i32 {
	let mut vec_fuel: Vec<i32> = Vec::with_capacity(data_clean.len());
	let vec_min = *data_clean.iter().min().unwrap();
	let vec_max = *data_clean.iter().max().unwrap();
	for itr_spot in vec_min..=vec_max {
		let mut fuel_new: i32 = 0;
		if flag_burn {
			fuel_new = data_clean.iter().map(|temp_num| burn(*temp_num, itr_spot)).sum();
		} else {
			fuel_new = data_clean.iter().map(|temp_num| (temp_num - itr_spot).abs()).sum();
		}
		vec_fuel.push(fuel_new);
	}
	return *vec_fuel.iter().min().unwrap();
}

// A condensed one line solve for day 7. Faster than non-meme solution, probably because a lack of a vector.
fn meme(data_clean: &Vec<i32>, flag_burn: bool) -> i32 {
	return (*data_clean.iter().min().unwrap()..=*data_clean.iter().max().unwrap()).map(|itr_spot| data_clean.iter().map(|temp_num| if flag_burn {(1..=(temp_num - itr_spot).abs()).sum()} else {(temp_num-itr_spot).abs()}).sum()).fold(i32::MAX, |a, b| a.min(b));
}

fn part1(data_clean: &Vec<i32>) -> i32 {
	return walk(data_clean, false);
}

fn part2(data_clean: &Vec<i32>) -> i32 {
	return walk(data_clean, true);
}

pub fn main() -> (i32, i32) {
	let file_raw = read::as_string("day7.txt");
	let file_data = clean(file_raw);
	return (part1(&file_data), part2(&file_data));
}
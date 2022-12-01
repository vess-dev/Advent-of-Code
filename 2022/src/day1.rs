use crate::read;

fn clean(file_data: &String) -> Vec<Vec<u32>> {
	return file_data.split("\n\n").map(|temp_x| temp_x.split("\n").map(|temp_y| temp_y.parse::<u32>().unwrap()).collect()).collect();
}

fn part1(data_clean: &Vec<Vec<u32>>) -> u32 {
	let mut sum_max = 0;
	for itr_x in data_clean {
		let sum_current = itr_x.iter().sum();
		if sum_current > sum_max {
			sum_max = sum_current;
		}
	}
	return sum_max;
}

fn part2(data_clean: &Vec<Vec<u32>>) -> u32 {
	let mut sum_vec: Vec<u32> = vec!();
	for itr_x in data_clean {
		let sum_current = itr_x.iter().sum();
		sum_vec.push(sum_current);
	}
	sum_vec.sort();
	return sum_vec.iter().rev().take(3).sum();
}

pub fn main() -> (u32, u32) {
	let file_raw = read::as_string("day1.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
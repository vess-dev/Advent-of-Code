use crate::read;

fn clean(file_data: &String) -> Vec<Vec<u8>> {
	return file_data.split("\n")
		.map(|temp_group| temp_group.split(&[',', '-'])
			.map(|temp_num| temp_num.parse::<u8>().unwrap())
			.collect())
		.collect();
}

fn is_inside(pair_1: (u8, u8), pair_2: (u8, u8)) -> bool {
	if ((pair_1.0 >= pair_2.0) && (pair_1.1 <= pair_2.1)) || ((pair_2.0 >= pair_1.0 && pair_2.1 <= pair_1.1)) {
		return true;
	}
	return false;
}

fn is_overlap(pair_1: (u8, u8), pair_2: (u8, u8)) -> bool {
	if ((pair_1.0 >= pair_2.0) && (pair_1.0 <= pair_2.1)) || ((pair_1.1 >= pair_2.0) && (pair_1.1 <= pair_2.1)) {
		return true;
	}
	return false;
}

fn part1(data_clean: &Vec<Vec<u8>>) -> u16 {
	let mut count_total = 0;
	for itr_line in data_clean {
		if is_inside((itr_line[0], itr_line[1]), (itr_line[2], itr_line[3])) {
			count_total += 1;
		}
	}
	return count_total;
}

fn part2(data_clean: &Vec<Vec<u8>>) -> u16 {
	let mut count_total = 0;
	for itr_line in data_clean {
		if is_overlap((itr_line[0], itr_line[1]), (itr_line[2], itr_line[3])) {
			count_total += 1;
		} else if is_inside((itr_line[0], itr_line[1]), (itr_line[2], itr_line[3])) {
			count_total += 1;
		}
	}
	return count_total;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day4.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
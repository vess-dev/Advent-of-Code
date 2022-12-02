use crate::read;

fn clean(file_data: &String) -> Vec<(char, char)> {
	return file_data.split("\n").map(|temp_line| (temp_line.chars().nth(0).unwrap(), temp_line.chars().nth(2).unwrap())).collect();
}

fn part1(data_clean: &Vec<(char, char)>) -> u16 {
	let mut score_total = 0;
	for itr_line in data_clean {
		match itr_line {
			('A', 'X') => score_total += 3 + 1,
			('A', 'Y') => score_total += 6 + 2,
			('A', 'Z') => score_total += 0 + 3,
			('B', 'X') => score_total += 0 + 1,
			('B', 'Y') => score_total += 3 + 2,
			('B', 'Z') => score_total += 6 + 3,
			('C', 'X') => score_total += 6 + 1,
			('C', 'Y') => score_total += 0 + 2,
			('C', 'Z') => score_total += 3 + 3,
			_ => unreachable!(),
		}
	}
	return score_total;
}

fn part2(data_clean: &Vec<(char, char)>) -> u16 {
	let mut score_total = 0;
	for itr_line in data_clean {
		match itr_line {
			('A', 'X') => score_total += 0 + 3,
			('A', 'Y') => score_total += 3 + 1,
			('A', 'Z') => score_total += 6 + 2,
			('B', 'X') => score_total += 0 + 1,
			('B', 'Y') => score_total += 3 + 2,
			('B', 'Z') => score_total += 6 + 3,
			('C', 'X') => score_total += 0 + 2,
			('C', 'Y') => score_total += 3 + 3,
			('C', 'Z') => score_total += 6 + 1,
			_ => unreachable!(),
		}
	}
	return score_total;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day2.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
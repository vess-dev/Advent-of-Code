use crate::read;

fn clean(file_data: &String) -> Vec<u16> {
	return file_data.split("\n")
		.map(|temp_num| temp_num.parse().unwrap())
		.collect();
}

fn part1(data_clean: &Vec<u16>) -> u16 {
	let mut sonar_inc = 0;
	let mut sonar_last = None;
	for itr_num in data_clean {
		if let Some(sonar_ping) = sonar_last {
			if itr_num > sonar_ping {
				sonar_inc += 1;
			}
		}
		sonar_last = Some(itr_num);
	}
	return sonar_inc;
}

fn part2(data_clean: &Vec<u16>) -> u16 {
	let mut sonar_idx = 0;
	let mut sonar_inc = 0;
	while (sonar_idx + 3) < data_clean.len() {
		let sonar_first: u16 = data_clean[sonar_idx..sonar_idx+3].iter().sum();
		let sonar_second: u16 = data_clean[sonar_idx+1..sonar_idx+4].iter().sum();
		if sonar_second > sonar_first {
			sonar_inc += 1;
		}
		sonar_idx += 1;
	}
	return sonar_inc;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day1.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
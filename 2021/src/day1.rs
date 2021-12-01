use crate::read;

fn part1(file_data: &Vec<u16>) -> u16 {
	let mut sonar_inc = 0;
	let mut sonar_last = None;
	for itr_num in file_data {
		if let Some(sonar_ping) = sonar_last {
			if itr_num > sonar_ping {
				sonar_inc += 1;
			}
		}
		sonar_last = Some(itr_num);
	}
	return sonar_inc;
}

fn part2(file_data: &Vec<u16>) -> u16 {
	let mut sonar_idx = 0;
	let mut sonar_inc = 0;
	while (sonar_idx + 3) < file_data.len() {
		let sonar_pri: &u16 = &file_data[sonar_idx..sonar_idx+3].iter().sum();
		let sonar_sec: &u16 = &file_data[sonar_idx+1..sonar_idx+4].iter().sum();
		if sonar_sec > sonar_pri {
			sonar_inc += 1;
		}
		sonar_idx += 1;
	}
	return sonar_inc;
}

pub fn main() -> (u16, u16) {
	let file_data = read::as_u16("day1.txt");
	return (part1(&file_data), part2(&file_data));
}
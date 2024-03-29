use crate::read;

#[derive(Debug)]
enum Com {
	Forward(u8),
	Up(u8),
	Down(u8),
}

fn clean(file_data: &String) -> Vec<Com> {
	return file_data.split("\n")
		.map(|temp_dir| {
			let com_full: Vec<&str> = temp_dir.split(" ").collect();
			let com_num: u8 = com_full[1].parse().unwrap();
			if com_full[0] == "forward" {
				Com::Forward(com_num)
			} else if com_full[0] == "up" {
				Com::Up(com_num)
			} else if com_full[0] == "down" {
				Com::Down(com_num)
			} else {
				panic!();
			}
		})
		.collect();
}

fn part1(data_clean: &Vec<Com>) -> u32 {
	let mut sub_horiz = 0;
	let mut sub_depth = 0;
	for itr_com in data_clean {
		if let Com::Forward(sub_add) = itr_com {
			sub_horiz += *sub_add as u32;
		} else if let Com::Up(sub_sub) = itr_com {
			sub_depth -= *sub_sub as u32;
		} else if let Com::Down(sub_add) = itr_com {
			sub_depth += *sub_add as u32;
		}
	}
	return sub_horiz * sub_depth;
}

fn part2(data_clean: &Vec<Com>) -> u32 {
	let mut sub_aim = 0;
	let mut sub_horiz = 0;
	let mut sub_depth = 0;
	for itr_com in data_clean {
		if let Com::Forward(sub_add) = itr_com {
			sub_horiz += *sub_add as u32;
			sub_depth += sub_aim * (*sub_add as u32)
		} else if let Com::Up(sub_sub) = itr_com {
			sub_aim -= *sub_sub as u32;
		} else if let Com::Down(sub_add) = itr_com {
			sub_aim += *sub_add as u32;
		}
	}
	return sub_horiz * sub_depth;
}

pub fn main() -> (u32, u32) {
	let file_raw = read::as_string("day2.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
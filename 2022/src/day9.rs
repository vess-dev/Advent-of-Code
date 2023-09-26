use crate::read;
use itertools::Itertools;

#[derive(Debug)]
enum Com {
	UP(u8),
	DOWN(u8),
	LEFT(u8),
	RIGHT(u8),
}

fn clean(file_data: &String) -> Vec<Com> {
	let com_vec = file_data.split("\n")
		.map(|temp_line| temp_line.split(" ")
			.collect_tuple()
			.map(|(temp_com, temp_num)| {
				let com_num = temp_num.parse().unwrap();
				return match temp_com {
					"U" => Com::UP(com_num),
					"D" => Com::DOWN(com_num),
					"L" => Com::LEFT(com_num),
					"R" => Com::RIGHT(com_num),
					_ => unreachable!(),
				}
			}).unwrap())
		.collect();
	return com_vec;
}

fn part1(data_clean: &Vec<Com>) -> () {
	println!("{:?}", data_clean);
	return ();
}

fn part2(data_clean: &Vec<Com>) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day9.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
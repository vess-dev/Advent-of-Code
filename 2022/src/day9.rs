use crate::read;

enum Com {
	UP(u8),
	DOWN(u8),
	LEFT(u8),
	RIGHT(u8),
}

fn clean(file_data: &String) -> () {
	let com_vec = Vec::new();
	file_data.split("\n").map(|temp_line| temp_line.split(" ").map(|temp_com| {
		match temp_com[0] {
			"U" => 0,
			"D" => 0,
			"L" => 0,
			"R" => 0,
		}
	}));
	return ();
}

fn part1(data_clean: &()) -> () {
	return ();
}

fn part2(data_clean: &()) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day9.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
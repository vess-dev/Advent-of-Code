use crate::read;

struct Display {
	
}

fn clean(file_data: &String) -> () {
	return ();
}

fn part1(data_clean: &String) -> u16 {
	return data_clean.replace(" | ", "\n")
		.split("\n")
		.skip(1)
		.step_by(2)
		.collect::<Vec<&str>>()
		.join(" ")
		.split(" ")
		.filter(|temp_string| [2, 3, 4, 7].contains(&temp_string.len())).count() as u16;
}

fn part2(data_clean: &()) -> () {
	return ();
}

pub fn main() -> (u16, ()) {
	let file_raw = read::as_string("day8.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_raw), part2(&file_data));
}
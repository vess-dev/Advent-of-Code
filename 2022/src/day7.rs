use crate::read;

fn clean(file_data: &String) -> () {
	return ();
}

fn part1(data_clean: &()) -> () {
	return ();
}

fn part2(data_clean: &()) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day7.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
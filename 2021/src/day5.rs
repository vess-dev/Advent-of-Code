use crate::read;

fn clean(file_data: String) -> () {
	return ();
}

fn part1(file_data: &()) -> () {
	return ();
}

fn part2(file_data: &()) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_data = read::as_string("day4.txt");
	let file_clean = clean(file_data);
	return (part1(&file_clean), part2(&file_clean));
}
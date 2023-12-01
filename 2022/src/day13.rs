use crate::read;
use std::collections::VecDeque;

struct Packet {
	left: VecDeque<char>,
	right: VecDeque<char>,
}

fn clean(file_data: &String) -> Vec<Packet> {
	let mut vec_signal = Vec::new();
	file_data.split("\n\n")
		.for_each(|temp_pair| {
			let packet_pair: Vec<_> = temp_pair.split("\n").collect();
			let packet_left: VecDeque<char> = packet_pair[0].chars().collect();
			let packet_right: VecDeque<char> = packet_pair[1].chars().collect();
			let packet_final = Packet {
				left: packet_left,
				right: packet_right,
			};
			vec_signal.push(packet_final);
	});
	return vec_signal;
}

fn part1(data_clean: &Vec<Packet>) -> () {
	return ();
}

fn part2(data_clean: &Vec<Packet>) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day13.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
use crate::read;

#[derive(Clone, Copy, Default)]
struct Bit {
	count0: u32,
	count1: u32,
}

impl Bit {
	fn most(self) -> bool {
		return !(self.count0 > self.count1);
	}
}

fn clean(file_data: String) -> Vec<String> {
	return file_data.split("\n")
		.map(|temp_num| temp_num.to_string())
		.collect();
}

fn bits(file_data: &Vec<String>) -> Vec<Bit> {
	let mut vec_bits= vec![Bit::default(); file_data[0].chars().count()];
	for itr_num in file_data {
		let num_split: Vec<char> = itr_num.chars().collect();
		for itr_bit in num_split.iter().enumerate() {
			match itr_bit.1 {
				'0' => vec_bits[itr_bit.0].count0 += 1,
				'1' => vec_bits[itr_bit.0].count1 += 1,
				_ => panic!(),
			}
		}
	}
	return vec_bits;
}

fn filter(vec_data: &Vec<String>, char_bonk: char, bit_index: usize) -> Vec<String> {
	let mut vec_final = Vec::with_capacity(vec_data.len());
	for itr_num in vec_data {
		if itr_num.chars().nth(bit_index).unwrap() != char_bonk {
			vec_final.push(itr_num.clone());
		}
	}
	return vec_final;
}


fn rating(file_data: &Vec<String>, bit_flip: bool) -> String {
	let mut vec_all = file_data.clone();
	let mut itr_idx = 0;
	while vec_all.len() != 1 {
		let vec_bits = bits(&vec_all);
		if bit_flip {
			if vec_bits[itr_idx].most() {
				vec_all = filter(&vec_all, '0', itr_idx);
			} else {
				vec_all = filter(&vec_all, '1', itr_idx);
			}
		} else {
			if vec_bits[itr_idx].most()  {
				vec_all = filter(&vec_all, '1', itr_idx);
			} else {
				vec_all = filter(&vec_all, '0', itr_idx);
			}
		}
		itr_idx += 1;
	}
	return vec_all[0].clone();
}

fn part1(file_data: &Vec<String>) -> u32 {
	let vec_bits = bits(file_data);
	let str_len = file_data[0].len();
	let mut final_epsilon = String::with_capacity(str_len);
	let mut final_gamma = String::with_capacity(str_len);
	for itr_bit in vec_bits {
		if itr_bit.most() {
			final_gamma.push('1');
			final_epsilon.push('0');
		}
		else {
			final_gamma.push('0');
			final_epsilon.push('1');
		}
	}
	let int_epsilon = u32::from_str_radix(&final_epsilon, 2).unwrap();
	let int_gamma = u32::from_str_radix(&final_gamma, 2).unwrap();
	return int_epsilon * int_gamma;
}

fn part2(file_data: &Vec<String>) -> u32 {
	let rating_oxy = rating(&file_data, true);
	let rating_scrub = rating(&file_data, false);
	let int_oxy = u32::from_str_radix(&rating_oxy, 2).unwrap();
	let int_scrub = u32::from_str_radix(&rating_scrub, 2).unwrap();
	return int_oxy * int_scrub;
}

pub fn main() -> (u32, u32) {
	let file_data = read::as_string("day3.txt");
	let file_clean = clean(file_data);
	return (part1(&file_clean), part2(&file_clean));
}
use crate::read;
use evalexpr::*;
use itertools::Itertools;
use std::collections::VecDeque;

#[derive(Clone)]
struct Monk {
	bag: VecDeque<u64>,
	oper: String,
	divi: u8,
	testt: usize,
	testf: usize,
	active: u32,
}

fn clean(file_data: &String) -> VecDeque<Monk> {
	let mut monk_vec = VecDeque::new();
	let monk_list = file_data.split("\n\n");
	for temp_monk in monk_list {
		let monk_data: Vec<_> = temp_monk.split("\n").collect();
		let monk_bag = monk_data[1].split(": ").nth(1).unwrap().split(", ").map(|temp_val| temp_val.parse().unwrap()).collect();
		let monk_oper = monk_data[2].split("= ").nth(1).unwrap().to_string();
		let monk_divi = monk_data[3].split("by ").nth(1).unwrap().parse().unwrap();
		let monk_testt = monk_data[4].split("monkey ").nth(1).unwrap().parse().unwrap();
		let monk_testf = monk_data[5].split("monkey ").nth(1).unwrap().parse().unwrap();
		let monk_new = Monk {
			bag: monk_bag,
			oper: monk_oper,
			divi: monk_divi,
			testt: monk_testt,
			testf: monk_testf,
			active: 0,
		};
		monk_vec.push_back(monk_new);
	}
	return monk_vec;
}

enum Worry {
	DIVI(f64),
	MOD(u64),
}

fn circlejerk(input_vec: &VecDeque<Monk>, input_loop: u32, input_worry: Worry) -> u64 {
	let mut monk_vec = input_vec.clone();
	for temp_round in 0..input_loop {
		for temp_idx in 0..monk_vec.len() {
			let mut monk_copy = monk_vec[temp_idx].clone();
			while !monk_copy.bag.is_empty() {
				let mut bag_item = monk_copy.bag.pop_front().unwrap();
				let oper_string = monk_copy.oper.replace("old", &bag_item.to_string());
				bag_item = eval_int(&oper_string).unwrap() as u64;
				match input_worry {
					Worry::DIVI(temp_worry) => bag_item = (bag_item as f64 / temp_worry).floor() as u64,
					Worry::MOD(temp_worry) => bag_item = (bag_item % temp_worry),
				}
				if bag_item % (monk_copy.divi as u64) == 0 {
					monk_vec[monk_copy.testt].bag.push_back(bag_item);
				} else {
					monk_vec[monk_copy.testf].bag.push_back(bag_item);
				}
				monk_copy.active += 1;
			}
			monk_vec[temp_idx] = monk_copy;
		}
	}
	monk_vec = monk_vec.into_iter().sorted_by_key(|temp_monk| temp_monk.active).rev().collect();
	let monk_busy = (monk_vec[0].active as u64) * (monk_vec[1].active as u64);
	return monk_busy;
}

fn part1(data_clean: &VecDeque<Monk>) -> u64 {
	let monk_twenty = circlejerk(data_clean, 20, Worry::DIVI(3.0));
	return monk_twenty;
}

fn part2(data_clean: &VecDeque<Monk>) -> u64 {
	let mut monk_lcm = 1u64;
	for temp_idx in 0..data_clean.len() {
		monk_lcm *= (data_clean[temp_idx].divi as u64);
	}
	let monk_tenthou = circlejerk(data_clean, 10000, Worry::MOD(monk_lcm));
	return monk_tenthou;
}

pub fn main() -> (u64, u64) {
	let file_raw = read::as_string("day11.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
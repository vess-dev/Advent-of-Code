use crate::read;
use std::collections::HashMap;

fn clean(file_data: &String) -> (HashMap<(char, char), u64>, HashMap<(char, char), char>, HashMap<char, u64>) {
	let mut data_split = file_data.split("\n\n");
	let mut poly_template = HashMap::new();
	let poly_orig = data_split.next().unwrap();
	poly_orig.chars().collect::<Vec<char>>().windows(2).for_each(|temp_pair| {
		let poly_pair = (temp_pair[0], temp_pair[1]);
		let poly_entry = poly_template.entry(poly_pair).or_insert(0);
		*poly_entry += 1;
	});
	let mut poly_rules = HashMap::new();
	data_split.next().unwrap().split("\n").map(|temp_rule| temp_rule.split(" -> ")).for_each(|mut temp_rule| {
		let mut rule_pair = temp_rule.next().unwrap().chars();
		poly_rules.entry((rule_pair.next().unwrap(), rule_pair.next().unwrap())).or_insert(temp_rule.next().unwrap().chars().next().unwrap());
	});
	let mut poly_total = HashMap::new();
	poly_orig.chars().for_each(|temp_char| {
		let poly_ref = poly_total.entry(temp_char).or_insert(0);
		*poly_ref += 1;
	});
	return (poly_template, poly_rules, poly_total);
}

fn step(step_count: u8, data_clean: &(HashMap<(char, char), u64>, HashMap<(char, char), char>, HashMap<char, u64>)) -> u64 {
	let mut poly_prev = data_clean.0.clone();
	let mut poly_total = data_clean.2.clone();
	for itr_step in 0..step_count {
		let mut poly_next = poly_prev.clone();
		for itr_pair in poly_prev.keys() {
			let poly_count = *poly_prev.get(itr_pair).unwrap();
			let poly_ref = poly_next.get_mut(itr_pair).unwrap();
			*poly_ref -= poly_count;
			let poly_insert = *data_clean.1.get(itr_pair).unwrap();
			let poly_fpair = poly_next.entry((itr_pair.0, poly_insert)).or_insert(0);
			*poly_fpair += poly_count;
			let poly_spair = poly_next.entry((poly_insert, itr_pair.1)).or_insert(0);
			*poly_spair += poly_count;
			let poly_ref = poly_total.entry(poly_insert).or_insert(0);
			*poly_ref += poly_count;
		}
		poly_prev = poly_next;
	}
	return poly_total.values().max().unwrap() - poly_total.values().min().unwrap();
}

fn part1(data_clean: &(HashMap<(char, char), u64>, HashMap<(char, char), char>, HashMap<char, u64>)) -> u64 {
	return step(10, data_clean);
}

fn part2(data_clean: &(HashMap<(char, char), u64>, HashMap<(char, char), char>, HashMap<char, u64>)) -> u64 {
	return step(40, data_clean);
}

pub fn main() -> (u64, u64) {
	let file_raw = read::as_string("day14.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
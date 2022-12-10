use crate::read;

fn clean(file_data: &String) -> (Vec<Vec<char>>, Vec<(u8, u8, u8)>) {
	let orders_split: Vec<_> = file_data.split("\n\n").collect();
	let mut orders_config: Vec<_> = orders_split[0].split("\n").collect();
	let orders_max = orders_config.pop().unwrap().split("   ").collect::<Vec<_>>().pop().unwrap().trim().parse::<u8>().unwrap();
	let mut orders_stacks: Vec<Vec<char>> = (1..=orders_max).into_iter().map(|_| vec![]).collect();
	orders_config.reverse();
	for itr_line in &orders_config {
		for itr_pair in itr_line.chars().skip(1).step_by(4).enumerate() {
			if itr_pair.1 != ' ' {
				orders_stacks[itr_pair.0].push(itr_pair.1);
			}
		}
	}
	let orders_list: Vec<_> = orders_split[1].split("\n").collect();
	let mut orders_final = vec![];
	for itr_order in orders_list {
		let order_vec: Vec<_> = itr_order.split(" ").collect();
		orders_final.push((order_vec[1].parse::<u8>().unwrap(), order_vec[3].parse::<u8>().unwrap(), order_vec[5].parse::<u8>().unwrap()))
	}
	return (orders_stacks, orders_final);
}

fn process_move(move_repeat: u8, order_input: u8, order_output: u8, orders_stacks: &mut Vec<Vec<char>>) {
	for itr_rep in 0..move_repeat {
		let stack_crate = orders_stacks[(order_input - 1) as usize].pop().unwrap();
		orders_stacks[(order_output - 1) as usize].push(stack_crate);
	}
}

fn process_load(move_size: u8, order_input: u8, order_output: u8, orders_stacks: &mut Vec<Vec<char>>) {
	let move_pos = orders_stacks[(order_input - 1) as usize].len() - (move_size as usize);
	let crates_load = orders_stacks[(order_input - 1) as usize].split_off((move_pos) as usize);
	for itr_crate in &crates_load {
		orders_stacks[(order_output - 1) as usize].push(*itr_crate);
	}
}

fn stack_tops(orders_stacks: &Vec<Vec<char>>) -> String {
	let mut string_final = String::new();
	for itr_stack in orders_stacks {
		string_final.push(*itr_stack.last().unwrap());
	}
	return string_final;
}

fn part1(data_clean: &(Vec<Vec<char>>, Vec<(u8, u8, u8)>)) -> String {
	let mut orders_stacks = data_clean.0.clone();
	for itr_order in &data_clean.1 {
		process_move(itr_order.0, itr_order.1, itr_order.2, &mut orders_stacks)
	}
	return stack_tops(&orders_stacks);
}

fn part2(data_clean: &(Vec<Vec<char>>, Vec<(u8, u8, u8)>)) -> String {
	let mut orders_stacks = data_clean.0.clone();
	for itr_order in &data_clean.1 {
		process_load(itr_order.0, itr_order.1, itr_order.2, &mut orders_stacks)
	}
	return stack_tops(&orders_stacks);
}

pub fn main() -> (String, String) {
	let file_raw = read::as_string("day5.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
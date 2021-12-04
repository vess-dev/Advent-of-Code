use crate::read;

#[derive(Clone, Debug)]
struct Board {
	moves_done: Vec<u8>,
	board_state: Vec<u8>,
}

impl Board {
	fn new(moves_size: &usize, board_data: &Vec<u8>) -> Self {
		return Board {
			moves_done: Vec::with_capacity(moves_size.clone()),
			board_state: board_data.clone(),
		};
	}

	fn update(&mut self, moves_next: &u8) {
		self.moves_done.push(moves_next.clone());
	}

	fn check(&self) -> bool {
		for itr_row in self.board_state.chunks(5) {
			if itr_row.iter().all(|temp_num| self.moves_done.contains(temp_num)) {
				return true;
			}
		}
		for itr_col in self.board_state.chunks(5){
			println!("{:?}", itr_col);
		}
		return false;
	}

	fn score(&self) -> u32 {
		let score_mult = *self.moves_done.last().unwrap() as u32;
		let mut score_sum: u32 = 0;
		for itr_num in &self.board_state {
			if !self.moves_done.contains(&itr_num) {
				score_sum += *itr_num as u32;
			}
		}
		return score_sum * score_mult;
	}
}

fn clean(file_data: String) -> (Vec<u8>, Vec<Board>) {
	let mut data_string = file_data.replace("  ", " ");
	data_string = data_string.replace("\n ", "\n");
	let data_raw: Vec<&str> = data_string.split("\n\n").collect();
	let data_moves: Vec<u8> = data_raw[0].split(",").collect::<Vec<&str>>().iter().rev().map(|temp_num| temp_num.parse::<u8>().unwrap()).collect();
	let mut data_boards = Vec::with_capacity(data_raw.len()-1);
	for itr_board in data_raw.iter().skip(1) {
		let data_board: Vec<u8> = itr_board.replace("\n", " ").split(" ").map(|temp_num| temp_num.parse::<u8>().unwrap()).collect();
		data_boards.push(Board::new(&data_moves.len(), &data_board));
	}
	return (data_moves, data_boards);
}

fn part1(data_clean: &(Vec<u8>, Vec<Board>)) -> u32 {
	let mut vec_moves = data_clean.0.to_vec();
	let mut vec_boards = data_clean.1.to_vec();
	println!("{:?}", vec_boards);
	vec_boards[0].check();
	panic!();
	while !vec_boards.iter().any(|temp_board| temp_board.check()) {
		let moves_next = vec_moves.pop().unwrap();
		vec_boards.iter_mut().for_each(|temp_board| temp_board.update(&moves_next));
	};
	for itr_board in vec_boards {
		if itr_board.check() {
			return itr_board.score();
		}
	}
	return 0;
}

fn part2(data_clean: &(Vec<u8>, Vec<Board>)) -> u32 {
//	let mut vec_moves = data_clean.0.to_vec();
//	let mut vec_boards = data_clean.1.to_vec();
//	let mut data_fin = Vec::with_capacity(vec_boards.len());
//	loop {
//		let mut data_rep = Vec::with_capacity(data_clean.len());
//		for itr_board in vec_boards.iter_mut() {
//			itr_board.update();
//			if itr_board.check() {
//				data_fin.push(itr_board.clone());
//			} else {
//				data_rep.push(itr_board.clone());
//			}
//		}
//		if data_rep.is_empty() {
//			break;
//		}
//		vec_boards = data_rep;
//	}
//	return data_fin.last().unwrap().score();
	return 3;
}

pub fn main() -> (u32, u32) {
	let file_raw = read::as_string("day4.txt");
	let file_data = clean(file_raw);
	return (part1(&file_data), part2(&file_data));
}
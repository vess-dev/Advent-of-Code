use crate::read;
use itertools::Itertools;
use std::collections::HashSet;

#[derive(Debug)]
enum Com {
	UP(u8),
	DOWN(u8),
	LEFT(u8),
	RIGHT(u8),
}

#[derive(Debug)]
struct Rope {
	posx: i16,
	posy: i16,
	tail: Option<Box<Rope>>,
	history: HashSet<(i16, i16)>,
}

impl Rope {

	fn new(rope_depth: u8) -> Rope {
		return Rope {
			posx: 0,
			posy: 0,
			tail: match rope_depth {
				0 => None,
				_ => Some(Box::new(Rope::new(rope_depth - 1))),
			},
			history: HashSet::from([(0, 0)]),
		};
	}

	fn pull(&mut self, com_next: &Com) -> () {
		let mut pull_dist = 0;
		match com_next {
			Com::UP(temp_dist) => pull_dist = *temp_dist,
			Com::DOWN(temp_dist) => pull_dist = *temp_dist,
			Com::LEFT(temp_dist) => pull_dist = *temp_dist,
			Com::RIGHT(temp_dist) => pull_dist = *temp_dist,
		}
		for temp_itr in 0..pull_dist {
			match com_next {
				Com::UP(_) => self.posy -= 1,
				Com::DOWN(_) => self.posy += 1,
				Com::LEFT(_) => self.posx -= 1,
				Com::RIGHT(_) => self.posx += 1,
			}
			self.tail.as_mut().unwrap().follow((self.posx, self.posy));
		}
	}

	fn follow(&mut self, head_pos: (i16, i16)) -> () {
		let head_dist = Self::dist((self.posx, self.posy), head_pos);
		if head_dist > 1.5 {
			if head_pos.0 < self.posx {
				self.posx -= 1;
			} else if head_pos.0 > self.posx {
				self.posx += 1;
			}
			if head_pos.1 < self.posy {
				self.posy -= 1;
			} else if head_pos.1 > self.posy {
				self.posy += 1;
			}
		}
		self.history.insert((self.posx, self.posy));
		if self.tail.is_some() {
			self.tail.as_mut().unwrap().follow((self.posx, self.posy));
		}
		return;
	}

	fn dist(pos_base: (i16, i16), pos_targ: (i16, i16)) -> f32 {
		let comp_x = (pos_targ.0 as f32 - pos_base.0 as f32);
		let comp_y = (pos_targ.1 as f32 - pos_base.1 as f32);
		let comp_total = comp_x.powf(2.0) + comp_y.powf(2.0);
		return comp_total.sqrt();
	}

	fn last(&self) -> &Rope {
		if self.tail.is_some() {
			return self.tail.as_ref().unwrap().last();
		}
		return &self;
	}

}

fn clean(file_data: &String) -> Vec<Com> {
	let com_vec = file_data.split("\n")
		.map(|temp_line| temp_line.split(" ")
			.collect_tuple()
			.map(|(temp_com, temp_num)| {
				let com_num = temp_num.parse().unwrap();
				return match temp_com {
					"U" => Com::UP(com_num),
					"D" => Com::DOWN(com_num),
					"L" => Com::LEFT(com_num),
					"R" => Com::RIGHT(com_num),
					_ => unreachable!(),
				}
			}).unwrap())
		.collect();
	return com_vec;
}

fn part1(data_clean: &Vec<Com>) -> u16 {
	let mut rope_head = Rope::new(1);
	for temp_com in data_clean {
		rope_head.pull(temp_com);
	}
	return rope_head.tail.as_ref().unwrap().history.len() as u16;
}

fn part2(data_clean: &Vec<Com>) -> u16 {
	let mut rope_head = Rope::new(9);
	for temp_com in data_clean {
		rope_head.pull(temp_com);
	}
	let rope_tail = rope_head.last();
	return rope_tail.history.len() as u16;
}

pub fn main() -> (u16, u16) {
	let file_raw = read::as_string("day9.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
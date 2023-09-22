use crate::read;
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::{Weak, Rc};

type RefDir = Rc<RefCell<Dir>>;
type RefParent = Weak<RefCell<Dir>>;

#[derive(Debug)]
enum Type {
	Dir(RefDir),
	File(File),
}

#[derive(Debug)]
struct Dir {
	parent: Option<RefParent>,
	children: HashMap<String, Type>,
	name: String,
	size: u32,
}

#[derive(Debug)]
struct File {
	name: String,
	size: u32,
}

impl Dir {
	fn new(dir_parent: Option<RefParent>, dir_name: &str) -> Dir {
		return Dir {
			parent: dir_parent,
			children: HashMap::new(),
			name: dir_name.to_string(),
			size: 0,
		};
	}

	fn get(&self, dir_name: &str) -> Option<RefDir> {
		let mut ref_dir = None;
		for temp_dir in &self.children {
			ref_dir = match temp_dir {
				Type::Dir(handle_dir) if handle_dir.borrow().name == dir_name => Some(Rc::clone(&handle_dir)),
				_ => None,
			};
			if let Some(_) = ref_dir {
				break;
			}
		}
		return ref_dir;
	}
	
	fn push(&mut self, child_new: Type) -> () {
		match &child_new {
			Type::Dir(handle_type) => self.size += handle_type.borrow().size,
			Type::File(handle_type) => self.size += handle_type.size,
		}
		self.children.push(child_new);
		return;
	}
}

fn clean(file_data: &String) -> () {
	let dir_root = Rc::new(RefCell::new(Dir::new(None, "/")));
	let mut dir_curr = Rc::clone(&dir_root);
	let dir_data: Vec<Vec<&str>> = file_data.split("\n").map(|temp_line| temp_line.split(" ").collect::<Vec<&str>>()).collect();
	let mut itr_index = 0;
	while itr_index != dir_data.len() {
		let com_split = &dir_data[itr_index];
		println!("{:?}", com_split);
		if com_split[0] == "$" {
			if com_split[1] == "cd" {
				if com_split[2] == "/" {
					dir_curr = Rc::clone(&dir_root);
				} else if com_split[2] == ".." {
					let dir_ref = dir_curr.borrow().parent.clone().unwrap();
					dir_curr = dir_ref.upgrade().unwrap();
				} else {
					let dir_ref = dir_curr.borrow().get(com_split[2]).unwrap();
					dir_curr = dir_ref;
				}
			}
			else if com_split[1] == "ls" {
				itr_index += 1;
				while itr_index != dir_data.len() {
					if dir_data[itr_index][0] == "$" {
						break;
					}
					else if &dir_data[itr_index][0] == &"dir" {
						let dir_new = Dir::new(Some(Rc::downgrade(&dir_curr)), dir_data[itr_index][1]);
						let dir_box = Type::Dir(Rc::new(RefCell::new(dir_new)));
						dir_curr.as_ref().borrow_mut().push(dir_box);
					} else {
						let dir_size = dir_data[itr_index][0].parse().unwrap();
						dir_curr.as_ref().borrow_mut().push(Type::File(File {name: dir_data[itr_index][1].to_string(), size: dir_size}));
					}
					itr_index += 1;
				}
				itr_index -= 1;
			}
		}
		itr_index += 1;
	}
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
	//return (part1(&file_data), part2(&file_data));
	return (part1(&file_data), part2(&file_data));
}
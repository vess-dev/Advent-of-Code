use crate::read;
use std::borrow::BorrowMut;
use std::cell::RefCell;
use std::collections::HashMap;
use std::rc::{Weak, Rc};

type RefDir = Rc<RefCell<Dir>>;
type RefParent = Weak<RefCell<Dir>>;

enum Type {
	Dir(RefDir),
	File(File),
}

struct Dir {
	parent: Option<RefParent>,
	children: HashMap<String, Type>,
	name: String,
	size: u32,
}

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
		let dir_handle = self.children.get(dir_name).unwrap();
		let mut dir_ref = None;
		dir_ref = match dir_handle {
			Type::Dir(dir_handle) if dir_handle.borrow().name == dir_name => Some(Rc::clone(&dir_handle)),
			_ => None,
		};
		return dir_ref;
	}
	
	fn push(&mut self, child_name: &str, child_new: Type) -> () {
		let mut type_size = 0;
		match &child_new {
			Type::Dir(type_handle) => type_size = type_handle.borrow().size,
			Type::File(type_handle) => type_size = type_handle.size,
		}
		self.size += type_size;
		let mut dir_parent = self.parent.clone();
		while let Some(_) = dir_parent {
			let dir_ref = dir_parent.as_ref().unwrap().upgrade().unwrap();
			dir_ref.as_ref().borrow_mut().size += type_size;
			dir_parent = dir_ref.borrow().parent.clone();
		}
		self.children.insert(child_name.to_string(), child_new);
		return;
	}
}

fn clean(file_data: &String) -> RefDir {
	let dir_root = Rc::new(RefCell::new(Dir::new(None, "/")));
	let mut dir_curr = Rc::clone(&dir_root);
	let dir_data: Vec<Vec<&str>> = file_data.split("\n").map(|temp_line| temp_line.split(" ").collect::<Vec<&str>>()).collect();
	let mut itr_index = 0;
	while itr_index != dir_data.len() {
		let com_split = &dir_data[itr_index];
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
					if &dir_data[itr_index][0] == &"$" {
						break;
					}
					else if &dir_data[itr_index][0] == &"dir" {
						let dir_name = dir_data[itr_index][1];
						let dir_new = Dir::new(Some(Rc::downgrade(&dir_curr)), dir_name);
						let dir_box = Type::Dir(Rc::new(RefCell::new(dir_new)));
						dir_curr.as_ref().borrow_mut().push(dir_name, dir_box);
					} else {
						let file_name = dir_data[itr_index][1];
						let file_size = dir_data[itr_index][0].parse().unwrap();
						dir_curr.as_ref().borrow_mut().push(file_name, Type::File(File {name: file_name.to_owned(), size: file_size}));
					}
					itr_index += 1;
				}
				itr_index -= 1;
			}
		}
		itr_index += 1;
	}
	return dir_root;
}

fn part1(data_clean: &RefDir) -> () {
	return ();
}

fn part2(data_clean: &RefDir) -> () {
	return ();
}

pub fn main() -> ((), ()) {
	let file_raw = read::as_string("day7.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
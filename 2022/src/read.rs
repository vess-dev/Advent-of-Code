use std::fs;
use std::fs::metadata;

pub fn path_rela() -> &'static str {
	let dir_result = metadata("./input");
	if let Err(_) = dir_result {
		return "../../input/";
	} else {
		return "./input/";
	}
}

pub fn as_string(file_name: &str) -> String {
	let file_prepend = path_rela();
	let file_full = format!("{}{}", file_prepend, file_name);
	let file_data = fs::read_to_string(file_full).expect("File error!");
	return file_data;
}
#![allow(dead_code)]
#![allow(unreachable_code)]
#![allow(unused_assignments)]
#![allow(unused_parens)]
#![allow(unused_variables)] 

use std::time::Instant;

mod read;

mod day1;
mod day2;
mod day3;
mod day4;
mod day5;
mod day6;
mod day7;
mod day8;
mod day9;
mod day10;
mod day11;
mod day12;

enum FnSig<U16, U13, U1S, U32, U64, STR, USZ> {
	U16U16(fn() -> U16),
	U16U32(fn() -> U13),
	U16STR(fn() -> U1S),
	U32U32(fn() -> U32),
	U64U64(fn() -> U64),
	STRSTR(fn() -> STR),
	USZUSZ(fn() -> USZ),
}

fn time() {
	use FnSig::*;
	let vec_days = [U32U32(day1::main), U16U16(day2::main), U16U16(day3::main), U16U16(day4::main), STRSTR(day5::main), U16U16(day6::main), U32U32(day7::main), U16U32(day8::main), U16U16(day9::main), U16STR(day10::main), U64U64(day11::main), USZUSZ(day12::main)];
	let test_count = 10;
	let mut test_type = String::from("trial");
	if test_count > 1 {
		test_type.push('s');
	}
	let mut test_ret = String::new();
	let time_total = Instant::now();
	for itr_day in vec_days.iter().enumerate() {
		let time_now = Instant::now();
		for _temp_test in 0..test_count {
			test_ret = match itr_day.1 {
				U16U16(func_ref) => format!("{:?}", func_ref()),
				U16STR(func_ref) => format!("{:?}", func_ref()),
				U16U32(func_ref) => format!("{:?}", func_ref()),
				U32U32(func_ref) => format!("{:?}", func_ref()),
				U64U64(func_ref) => format!("{:?}", func_ref()),
				STRSTR(func_ref) => format!("{:?}", func_ref()),
				USZUSZ(func_ref) => format!("{:?}", func_ref()),
			};
		}
		let time_elapsed = time_now.elapsed().as_secs_f64();
		let time_day = itr_day.0 + 1;
		println!("Day {}: {}", time_day, test_ret);
		println!("{} {} of day {}: {:.7}s\n", test_count, test_type, time_day, (time_elapsed/test_count as f64));
	}
	let time_elapsed = time_total.elapsed().as_secs_f64();
	println!("{} {} of all, averages: {:.7} seconds.", test_count, test_type, (time_elapsed/test_count as f64)); 
}

fn main() {
	#[cfg(not(debug_assertions))]
	time();
	#[cfg(debug_assertions)]
	println!("{:?}", day12::main());
}
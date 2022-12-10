#![allow(dead_code)]
#![allow(unreachable_code)]
#![allow(unused_assignments)]
#![allow(unused_variables)] 

use std::time::Instant;

mod read;

mod day1;
mod day2;
mod day3;
mod day4;

enum FnSig<U16, U32> {
	U16U16(fn() -> U16),
	U32U32(fn() -> U32),
}

fn time() {
	use FnSig::*;
	let vec_days = [FnSig::U32U32(day1::main), FnSig::U16U16(day2::main), FnSig::U16U16(day3::main), FnSig::U16U16(day4::main)];
	let test_count = 10;
	let mut test_type = String::new();
	if test_count == 1 {
		test_type = String::from("trial");
	} else {
		test_type = String::from("trials");
	}
	let mut test_ret = String::new();
	let time_total = Instant::now();
	for itr_day in vec_days.iter().enumerate() {
		let time_now = Instant::now();
		for _temp_test in 0..test_count {
			test_ret = match itr_day.1 {
				U16U16(func_ref) => format!("{:?}", func_ref()),
				U32U32(func_ref) => format!("{:?}", func_ref()),
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
	println!("{:?}", day5::main());
}
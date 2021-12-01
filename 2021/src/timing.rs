#[allow(dead_code)]

use std::time::Instant;
use std::fmt::Display;
use std::fmt::Debug;

mod day1;
mod day2;

enum FnSig {

}

fn clock<T1: Debug, T2: Default>(test_count: u8, day_ref: &dyn Fn() -> Box<T1>) -> (f64, Box<T1>) {
    let time_now = Instant::now();
    let mut ret_var = Default::default();
    for _temp_test in 0..test_count {
        ret_var = day_ref();
    }
    return (time_now.elapsed().as_secs_f64(), ret_var);
}

fn main() {
    let vec_days: Vec<Box<dyn Fn () -> Box<dyn Debug + Default>>> = vec![Box::new(day1::main), Box::new(day2::main)];
    let test_count = 3;
    let time_total = Instant::now();
    for itr_day in vec_days.iter().enumerate() {
        let test_ret = clock(test_count, itr_day.1);
        println!("Day {}: {:?}", (itr_day.0)+1, test_ret.1);
        println!("{} trials of day {}: {}", test_count, itr_day.0, test_ret.0);
    }
}
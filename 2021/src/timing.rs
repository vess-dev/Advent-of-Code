#![allow(dead_code)]
#![allow(unused_imports)]

use std::time::Instant;

mod read;

mod day1;
mod day2;

enum FnSig<D1, D2> {
    U16U16(fn() -> D1),
    STRU32(fn() -> D2),
}

fn main() {
    use FnSig::*;
    let vec_days = vec![FnSig::U16U16(day1::main), FnSig::STRU32(day2::main)];
    let test_count = 100;
    let mut test_ret = String::new();
    let time_total = Instant::now();
    for itr_day in vec_days.iter().enumerate() {
        let time_now = Instant::now();
        for _temp_test in 0..test_count {
            test_ret = match itr_day.1 {
                U16U16(func_ref) => format!("{:?}", func_ref()),
                STRU32(func_ref) => format!("{:?}", func_ref()),
            };
        }
        let time_elapsed = time_now.elapsed().as_secs_f64();
        println!("Day {}: {}", (itr_day.0)+1, test_ret);
        println!("{} trials of day {}: {:.5}", test_count, itr_day.0, (time_elapsed/test_count as f64));
    }
    let time_elapsed = time_total.elapsed().as_secs_f64();
    println!("{} trials of all, averages: {:.5}", test_count, (time_elapsed/test_count as f64));
}
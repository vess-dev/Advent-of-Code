#![allow(dead_code)]
#![allow(unreachable_code)]
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

enum FnSig<T1, T2, T3, T4> {
    U16U16(fn() -> T1),
    U32U32(fn() -> T2),
    U64U64(fn() -> T3),
    USZUSZ(fn() -> T4),
}

fn time() {
   use FnSig::*;
    let vec_days = [FnSig::U16U16(day1::main), FnSig::U32U32(day2::main), FnSig::U32U32(day3::main), FnSig::U32U32(day4::main), FnSig::USZUSZ(day5::main), FnSig::U64U64(day6::main)];
    let test_count = 3;
    let mut test_ret = String::new();
    let time_total = Instant::now();
    for itr_day in vec_days.iter().enumerate() {
        let time_now = Instant::now();
        for _temp_test in 0..test_count {
            test_ret = match itr_day.1 {
                U16U16(func_ref) => format!("{:?}", func_ref()),
                U32U32(func_ref) => format!("{:?}", func_ref()),
                U64U64(func_ref) => format!("{:?}", func_ref()),
                USZUSZ(func_ref) => format!("{:?}", func_ref()),
            };
        }
        let time_elapsed = time_now.elapsed().as_secs_f64();
        let time_day = (itr_day.0)+1;
        println!("Day {}: {}", time_day, test_ret);
        println!("{} trials of day {}: {:.7}s\n", test_count, time_day, (time_elapsed/test_count as f64));
    }
    let time_elapsed = time_total.elapsed().as_secs_f64();
    println!("{} trials of all, averages: {:.7} seconds.", test_count, (time_elapsed/test_count as f64)); 
}

fn main() {
    #[cfg(not(debug_assertions))]
    time();
    #[cfg(debug_assertions)]
    println!("{:?}", day7::main());
}
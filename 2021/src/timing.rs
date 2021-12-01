#![allow(dead_code)]
#![allow(unused_imports)]

use std::time::Instant;

mod read;

mod day1;
mod day2;

enum FnSig {
    U32U32(fn() -> (u16, u16)),
    STRU32(fn() -> (String, u32)),
}

fn run<T1, T2>(func_sig: &FnSig) -> (T1, T2) {
    if let FnSig::U32U32(func_ref) = func_sig {
        return func_ref();
    } else if let FnSig::STRU32(func_ref) = func_sig {
        return func_ref();
    } else {
        return (0, 0)
    };
}

fn main() {
    let vec_days = vec![FnSig::U32U32(day1::main), FnSig::STRU32(day2::main)];
    let test_count = 3;
    let time_total = Instant::now();
    for itr_day in vec_days.iter().enumerate() {
        let time_now = Instant::now();
        for _temp_test in 1..test_count {
            run(itr_day.1);
        }
        let test_ret = run(itr_day.1);
        println!("Day {}: {:?}", (itr_day.0)+1, test_ret.1);
        println!("{} trials of day {}: {}", test_count, itr_day.0, time_now.elapsed().as_secs_f64());
    }
}
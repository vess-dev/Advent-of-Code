use crate::read;

fn clean(file_data: &String) -> [u64; 9] {
	let mut fish_arr = [0; 9];
	file_data.split(",")
		.map(|temp_num| temp_num.parse::<u8>().unwrap())
		.for_each(|temp_num| {
			fish_arr[temp_num as usize] += 1;
		});
	return fish_arr;
}

fn days(day_loop: u16, data_clean: &[u64; 9]) -> u64 {
	let mut fish_arr = data_clean.clone();
	for itr_day in 0..day_loop {
		let mut fish_new = [0; 9];
		for itr_fish in (0..=8).rev() {
			if itr_fish == 0 {
				fish_new[6] += fish_arr[0];
				fish_new[8] = fish_arr[0];
			} else {
				fish_new[itr_fish-1] = fish_arr[itr_fish];
			}	
		}
		fish_arr = fish_new;
	}
	return fish_arr.iter().sum();
}

fn part1(data_clean: &[u64; 9]) -> u64 {
	return days(80, data_clean);
	
}

fn part2(data_clean: &[u64; 9]) -> u64 {
	return days(256, data_clean);
}

pub fn main() -> (u64, u64) {
	let file_raw = read::as_string("day6.txt");
	let file_data = clean(&file_raw);
	return (part1(&file_data), part2(&file_data));
}
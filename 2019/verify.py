import day2
import day5
import day7
import day9
import day11
import day13
#import day15
#import day17
#import day19
#import day21
#import day23
#import day25

TEST_MAP = {
	day2:  ("Day 2", (2842648,    9074    )),
	day5:  ("Day 5", (6761139,    9217546 )),
	day7:  ("Day 7", (929800,     15432220)),
	day9:  ("Day 9", (3380552333, 78831   )),
	day11: ("Day 11", (1885,       None    )),
	day13: ("Day 13", (236,        11040   )),
}

def test():
	for temp_test in TEST_MAP.keys():
		test_tuple = TEST_MAP[temp_test]
		if temp_test == day11:
			test_run = temp_test.run(False)
		else:
			test_run = temp_test.run()
		test_string = f"{test_tuple[0]} : {test_tuple[1] == test_run} : {test_tuple[1]} , {test_run}"
		print(test_string)
	return

if __name__ == "__main__":
	test()
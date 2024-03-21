package main

import (
	
)

func dXclean(in_raw string) any {
	out_clean := in_raw
	return out_clean
}

func dXpart1(in_clean any) any {
	tdebug(in_clean)
	return -1
}

func dXpart2(in_clean any) any {
	tdebug(in_clean)
	return -1
}

func dayX() (any, any) {
	file_string := tload("input/dayX.txt")
	file_clean := dXclean(file_string)
	return dXpart1(file_clean), dXpart2(file_clean)
}
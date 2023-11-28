package main

import (
	"os"
	"strconv"
	"strings"
)

func dXclean(in_raw string) any {
	out_clean := in_raw 
	return out_clean
}

func dXpart1(in_clean any) any {
	return in_clean
}

func dXpart2(in_clean any) any {
	return in_clean
}

func dayX() (any, any) {
	file_data, file_error := os.ReadFile("input/dayX.txt")
	check(file_error)
	file_string := string(file_data)
	file_clean := dXclean(file_string)
	return dXpart1(file_clean), dXpart2(file_clean)
}
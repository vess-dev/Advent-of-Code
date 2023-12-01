package main

import (
	"os"
)

func tcheck(in_error error) {
	if in_error != nil {
		panic(in_error)
	}
}

func tload(in_path string) string {
	file_data, file_error := os.ReadFile("input/day1.txt")
	tcheck(file_error)
	return string(file_data)
}

func tuse(in_list ...any) {
	for _, temp_var := range in_list {
		_ = temp_var
	}
}
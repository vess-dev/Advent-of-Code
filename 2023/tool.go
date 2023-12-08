package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
	"slices"
	"strconv"
	"strings"
	"time"
)

func tcast(in_slice []string) []int {
	out_slice := make([]int, len(in_slice))
	for temp_idx, temp_string := range in_slice {
		int_data, int_error := strconv.Atoi(temp_string)
		tcheck(int_error)
		out_slice[temp_idx] = int_data
	}
	return out_slice
}

func tcheck(in_error error) {
	if in_error != nil {
		panic(in_error)
	}
}

func tconcatdigits(in_ints []int) int {
	ret_int := in_ints[0]
	for _, temp_int := range in_ints[1:] {
		ret_int *= 10
		ret_int += temp_int
	}
	return ret_int
}

func tconcatint(in_x int, in_y int) int {
	int_digits := tcountdigit(in_y)
	int_new := in_x * tpow(10, int_digits) + in_y
	return int_new
}

func tconcatgroup(in_ints []int) int {
	final_int := in_ints[0]
	for _, temp_int := range in_ints[1:] {
		final_int = tconcatint(final_int, temp_int)
	}
	return final_int
}

func tcopy[T any](in_var []T) []T {
	return slices.Clone(in_var)
}

func tcountdigit(in_int int) int {
	if (in_int == 0) {
		return 1;
	}
	int_current := in_int
	var ret_count int
	for {
		if (int_current != 0) {
			int_current = int_current / 10
			ret_count += 1
		} else {
			break
		}
	}
	return ret_count
}

func tdigit(in_string string) bool {
	switch in_string {
		case "0", "1", "2", "3", "4", "5", "6", "7", "8", "9": return true 
		default: return false
	}
}

func tdrop[T any](in_list []T, in_index int) []T {
	return append(in_list[:in_index], in_list[in_index+1:]...)
}

func tgcd(in_x int, in_y int) int {
	for in_y != 0 {
			var_t := in_y
			in_y = in_x % in_y
			in_x = var_t
	}
	return in_x
}

func tlcm(in_x int, in_y int, in_ints ...int) int {
	ret_lcm := in_x * in_y / tgcd(in_x, in_y)
	for temp_itr := 0; temp_itr < len(in_ints); temp_itr++ {
		ret_lcm = tlcm(ret_lcm, in_ints[temp_itr])
	}
	return ret_lcm
}

func tline(in_list ...any) {
	if len(in_list) == 0 {
		fmt.Println(strings.Repeat("=", 100))
	} else {
		for _, temp_var := range in_list[:len(in_list)-1] {
			fmt.Printf("%#v, ", temp_var)
		}
		fmt.Printf("%#v\n", in_list[len(in_list)-1])
	}
}

func tload(in_path string) string {
	file_data, file_error := os.ReadFile(in_path)
	tcheck(file_error)
	return string(file_data)
}

func tmake(in_fill any, in_len ...int) any {
	var slice_final []any
	if len(in_len) == 1 {
		for temp_itr := 1; temp_itr <= in_len[0]; temp_itr++ {
			slice_final = append(slice_final, in_fill)
		}
	} else {
		for temp_itr := 1; temp_itr <= in_len[0]; temp_itr++ {
			slice_next := tmake(in_fill, in_len[1:]...)
			slice_final = append(slice_final, slice_next)
		}
	}
	return slice_final
}

func tminidx(in_list []int) int {
	int_min := math.MaxInt
	int_idx := -1
	for temp_idx, temp_val := range in_list {
		if temp_val < int_min {
			int_min = temp_val
			int_idx = temp_idx
		}
	}
	return int_idx
}

func tpop(in_slice []any) (any, []any) {
	ret_pop, ret_slice := in_slice[0], in_slice[1:]
	return ret_pop, ret_slice
}

func tpow(in_base int, in_exp int) int {
	ret_result := 1
    for {
        if (in_exp & 1) == 1 {
            ret_result *= in_base
        }
        in_exp >>= 1
        if in_exp == 0 {
            break
        }
        in_base *= in_base
    }
    return ret_result
}

func tprint(in_list ...any) {
	if len(in_list) == 0 {
		fmt.Println()
	} else {
		for _, temp_var := range in_list {
			fmt.Printf("%#v\n", temp_var)
		}
	}
}

func trand(in_min int, in_max int) int {
	rand_int := rand.Intn(in_max - in_min) + in_min
	return rand_int
}

func tsleep(in_seconds int) {
	sleep_duration := time.Duration(in_seconds) * time.Second
	time.Sleep(sleep_duration)
}

func tstringints(in_ints []int) string {
	var int_string string
	for _, temp_int := range in_ints {
		int_string += fmt.Sprint(temp_int)
	}
	return int_string
}

func tuse(in_list ...any) {
	for _, temp_var := range in_list {
		_ = temp_var
	}
}

func tzip(in_x []any, in_y []any) [][]any {
	var int_zip [][]any
	for temp_idx := range in_x {
		int_zip = append(int_zip, []any{in_x[temp_idx], in_y[temp_idx]})
	}
	return int_zip
}
package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

func tabs(in_int int) int {
	if in_int < 0 {
		return -in_int
	}
	return in_int
}

func taddall[T comparable](in_map map[T]bool, in_new []T) map[T]bool {
	for _, temp_check := range in_new {
		if !in_map[temp_check] {
			in_map[temp_check] = true
		}
	}
	return in_map
}

func tappappnot[T comparable](in_slice []T, in_append []T, in_ref map[T]bool) []T {
	return tappslice(in_slice, tappnot(in_append, in_ref))
}

func tappslice[T any](in_slice []T, in_append []T) []T {
	return append(in_slice, in_append...)
}

func tappnot[T comparable](in_append []T, in_ref map[T]bool) []T {
	var slice_not []T
	for _, temp_check := range in_append {
		if !in_ref[temp_check] {
			slice_not = append(slice_not, temp_check)
		}
	}
	return slice_not
}

func tbin(in_num int, in_length int) []string {
	bin_format := strings.Replace("%0?b", "?", fmt.Sprint(in_length), 1)
	bin_string := fmt.Sprintf(bin_format, in_num)
	return strings.Split(bin_string, "")
}

func tcast(in_slice []string) []int {
	slice_ints := make([]int, len(in_slice))
	for temp_idx, temp_string := range in_slice {
		int_data := tnumf(temp_string)
		slice_ints[temp_idx] = int_data
	}
	return slice_ints
}

func tcharat(in_string string, in_pos int) string {
	return string([]rune(in_string)[in_pos])
}

func tcheck(in_error error) {
	if in_error != nil {
		panic(in_error)
	}
	return
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

func tcopy[T any](in_slice []T) []T {
	slice_new := make([]T, len(in_slice))
	for temp_idx, temp_item := range in_slice {
		slice_new[temp_idx] = temp_item
	}
	return slice_new
}

func tcopymap[T comparable, U any](in_map map[T]U) map[T]U {
	map_new := make(map[T]U, len(in_map))
	for temp_key, temp_value := range in_map {
		map_new[temp_key] = temp_value
	}
	return map_new
}

func tcount[T comparable](in_slice []T, in_match T) int {
	var match_count int
	for temp_idx := range in_slice {
		if in_slice[temp_idx] == in_match {
			match_count += 1
		}
	}
	return match_count
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

func tdebug(in_list ...any) {
	final_index := len(in_list)-1
	var final_string string
	for _, temp_var := range in_list[:final_index] {
		final_string += fmt.Sprintf("%#v, ", temp_var)
	}
	final_string += fmt.Sprintf("%#v", in_list[final_index])
	fmt.Println(final_string)
	return
}

func tdigit(in_string string) bool {
	switch in_string {
		case "0", "1", "2", "3", "4", "5", "6", "7", "8", "9": return true 
		default: return false
	}
}

func tdist(in_x1 int, in_y1 int, in_x2 int, in_y2 int) float64 {
	x_diff := tpow(in_x2 - in_x1, 2)
	y_diff := tpow(in_y2 - in_y1, 2)
	float_sum := float64(x_diff + y_diff)
	return math.Sqrt(float_sum)
}

func tdrop[T any](in_list []T, in_index int) []T {
	return append(in_list[:in_index], in_list[in_index+1:]...)
}

func tequal[T comparable](in_base []T, in_comp []T) bool {
	if len(in_base) != len(in_comp) {
		return false
	}
	for temp_idx, temp_value := range in_base {
		if temp_value != in_comp[temp_idx] {
			return false
		}
	}
	return true
}

func tequals[T comparable](in_base []T, in_comp []T) int {
	var total_diff int
	for temp_idx, temp_value := range in_base {
		if temp_value != in_comp[temp_idx] {
			total_diff += 1
		}
	}
	return total_diff
}

func teven(in_int int) bool {
	return (in_int & 1) == 0
}

func texit() {
	os.Exit(0)
}

func tgcd(in_x int, in_y int) int {
	for in_y != 0 {
			var_t := in_y
			in_y = in_x % in_y
			in_x = var_t
	}
	return in_x
}

func thas(in_item any, in_slice []any) bool {
	for _, temp_item := range in_slice {
		if in_item == temp_item {
			return true
		}
	}
	return false
}

func thextoint(in_hex string) int {
	parse_data, parse_error := strconv.ParseInt(in_hex, 16, 64)
	tcheck(parse_error)
	return int(parse_data)
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
		final_index := len(in_list)-1
		var final_string string
		for _, temp_var := range in_list[:final_index] {
			final_string += fmt.Sprintf("%v, ", temp_var)
		}
		final_string += fmt.Sprintf("%v", in_list[final_index])
		fmt.Println(final_string)
	}
	return
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

func tmax(in_x int, in_y int) int {
	if in_x > in_y {
		return in_x
	}
	return in_y
}

func tmin(in_x int, in_y int) int {
	if in_x < in_y {
		return in_x
	}
	return in_y
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

func tnln() {
	fmt.Println()
}

func tnum(in_string string) int {
	int_data, int_error := strconv.Atoi(in_string)
	tcheck(int_error)
	return int_data
}

func tnumf(in_string string) int {
	int_data, _ := strconv.Atoi(in_string)
	return int_data
}

func todd(in_int int) bool {
	return (in_int & 1) == 1
}

func tones(in_int int) int {
	var bit_sum int
	for in_int > 0 {
		in_int &= (in_int - 1)
		bit_sum += 1
	}
	return bit_sum
}

func tout(in_type any) {
	fmt.Print(in_type)
}

func tpop[T any](in_slice []T) (T, []T) {
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
		var final_string string
		for _, temp_var := range in_list {
			final_string += fmt.Sprintf("%v\n", temp_var)
		}
		fmt.Print(final_string)
	}
	return
}

func trand(in_min int, in_max int) int {
	rand_int := rand.Intn(in_max - in_min) + in_min
	return rand_int
}

func trune(in_rune string) rune {
	return []rune(in_rune)[0]
}

func trunes(in_runes string) []rune {
	return []rune(in_runes)
}

func tsame[T comparable](in_slice []T) bool {
	for _, temp_item := range in_slice[1:] {
		if in_slice[0] != temp_item {
			return false
		}
	}
	return true
}

func tshas(in_slice []any, in_check []any) bool {
	for _, temp_item := range in_slice {
		for _, temp_check := range in_check {
			if temp_item == temp_check {
				return true
			}
		}
	}
	return false
}

func tsign(in_int int) int {
	if in_int == 0 {
		return 0
	}
	return in_int / tabs(in_int)
}

func tsleep(in_seconds int) {
	sleep_duration := time.Duration(in_seconds) * time.Second
	time.Sleep(sleep_duration)
}

func tsnum(in_int int) string {
	return strconv.Itoa(in_int)
}

func tsteps(in_x1 int, in_y1 int, in_x2 int, in_y2 int) int {
	x_diff := tabs(in_x2 - in_x1)
	y_diff := tabs(in_y2 - in_y1)
	return x_diff + y_diff
}

func tstring(in_list ...any) string {
	var string_out string
	for _, temp_type := range in_list {
		string_out += fmt.Sprint(temp_type)
	}
	return string_out
}

func tsubstring(in_string string, in_start string, in_end string) string {
    index_start := strings.Index(in_string, in_start)
    if index_start == -1 {
        return ""
    }
    index_end := strings.Index(in_string[index_start:], in_end)
    if index_end == -1 {
        return ""
    }
    return in_string[index_start+len(in_start):index_end+index_start]
}

func tsum(in_ints []int) int {
	var final_sum int
	for _, temp_int := range in_ints {
		final_sum += temp_int
	}
	return final_sum
}

func tsummap[T comparable](in_map map[T]int) int {
	var final_sum int
	for _, temp_value := range in_map {
		final_sum += temp_value
	}
	return final_sum
}
func ttern[T any](in_cond bool, in_true T, in_false T) T {
    if in_cond {
        return in_true
    }
    return in_false
}

func tuse(in_list ...any) {
	for _, temp_var := range in_list {
		_ = temp_var
	}
}

func twait() {
	fmt.Scanln()
}

func tzip(in_x []any, in_y []any) [][]any {
	var int_zip [][]any
	for temp_idx := range in_x {
		int_zip = append(int_zip, []any{in_x[temp_idx], in_y[temp_idx]})
	}
	return int_zip
}
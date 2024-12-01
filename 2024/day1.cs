namespace aoc2024;

using ListPair = (List<int>, List<int>);
using DayAlias = Day<(List<int>, List<int>), (List<int>, List<int>), int, int>;

public class Day1 : DayAlias {

    public (ListPair, ListPair) Prepare(string in_string) {
        List<int> int_list1 = new List<int>();
        List<int> int_list2 = new List<int>();
        var string_pairs = in_string.Split("\n");
        foreach (var temp_line in string_pairs) {
            var string_ints = temp_line.Split("   ");
            int_list1.Add(int.Parse(string_ints[0]));
            int_list2.Add(int.Parse(string_ints[1]));
        }
        return ((int_list1, int_list2), (int_list1, int_list2));
    }

    public int Part1(ListPair in_data) {
        in_data.Item1.Sort();
        in_data.Item2.Sort();
        int distance_total = 0;
        for (int temp_index = 0; temp_index < in_data.Item1.Count; temp_index++) {
            distance_total += Math.Abs(in_data.Item2[temp_index] - in_data.Item1[temp_index]);
        }
        return distance_total;
    }

    public int Part2(ListPair in_data) {
        int similar_score = 0;
        foreach (int temp_int in in_data.Item1) {
            similar_score += temp_int * in_data.Item2.Count(temp_item => temp_item == temp_int);
        }
        return similar_score;
    }

    public (object, object) Run() {
        var input_raw = Tool.LoadFile("input/day1.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.Item1), Part2(input_clean.Item2));
    }
}
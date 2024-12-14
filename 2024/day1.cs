namespace aoc2024;

using ListPair = (List<int> L, List<int> R);

public class Day1 : Day<(List<int> L, List<int> R), (List<int> L, List<int> R), int, int> {

    public (ListPair P1, ListPair P2) Prepare(string in_string) {
        var int_list1 = new List<int>();
        var int_list2 = new List<int>();
        var string_pairs = in_string.Split("\n");
        foreach (var temp_line in string_pairs) {
            var string_ints = temp_line.Split("   ");
            int_list1.Add(int.Parse(string_ints[0]));
            int_list2.Add(int.Parse(string_ints[1]));
        }
        return ((int_list1, int_list2), (int_list1, int_list2));
    }

    public int Part1(ListPair in_data) {
        in_data.L.Sort();
        in_data.R.Sort();
        int distance_total = 0;
        for (int temp_index = 0; temp_index < in_data.L.Count; temp_index++) {
            distance_total += Math.Abs(in_data.L[temp_index] - in_data.R[temp_index]);
        }
        return distance_total;
    }

    public int Part2(ListPair in_data) {
        int similar_score = 0;
        var list_group = in_data.R.GroupBy(temp_int => temp_int)
            .ToDictionary(temp_group => temp_group.Key, temp_group => temp_group.Count());
        foreach (int temp_int in in_data.L) {
            list_group.TryGetValue(temp_int, out int compare_int);
            similar_score += temp_int * compare_int;
        }
        return similar_score;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day1.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
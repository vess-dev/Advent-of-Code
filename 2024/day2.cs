namespace aoc2024;

using LLInt = List<List<int>>;

public class Day2 : Day<List<List<int>>, List<List<int>>, int, int> {

    public (LLInt P1, LLInt P2) Prepare(string in_string) {
        var out_list = new LLInt();
        var string_lines = in_string.Split("\n");
        foreach (var temp_line in string_lines) {
            var string_split = temp_line.Split(" ");
            var out_line = string_split.Select(int.Parse).ToList();
            out_list.Add(out_line);
        }
        return (out_list, out_list);
    }

    private static bool Check(int in_one, int in_two, bool in_parabola) {
        return in_one < in_two == in_parabola && Math.Abs(in_one - in_two).Between(1, 3);
    }

    private static bool CheckList(List<int> in_list) {
        return in_list.Zip(in_list.Skip(1))
            .All(temp_pair => {
                var parabola_bool = in_list[0] < in_list[1];
                return Check(temp_pair.Item1, temp_pair.Item2, parabola_bool);
            });
    }

    public int Part1(LLInt in_data) {
        return in_data
            .Count(CheckList);
    }
    
    public int Part2(LLInt in_data) {
        var safe_total = 0;
        foreach (var temp_line in in_data) {
            var check_index = temp_line.Zip(temp_line.Skip(1)).ToList()
                .FindIndex(temp_set => {
                    var parabola_bool = temp_line[0] < temp_line[1];
                    return !Check(temp_set.Item1, temp_set.Item2, parabola_bool);
                });
            if (check_index == -1) {
                safe_total += 1;
                continue;
            }
            for (var temp_itr = check_index - 1; temp_itr <= check_index + 1; temp_itr++) {
                var test_line = temp_line.Where((temp_value, temp_index) => temp_index != temp_itr).ToList();
                if (CheckList(test_line)) {
                    safe_total += 1;
                    break;
                }
            }
        }
        return safe_total;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day2.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
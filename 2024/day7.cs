namespace aoc2024;

using ListOp = List<Day7.Oper>;

public class Day7 : Day<List<Day7.Oper>, List<Day7.Oper>, long, long> {

    public class Oper {
        public long number_checksum;
        public List<long> number_list = new();

        public bool Dig(List<long> in_list, long in_sum, bool in_cat) {
            if (in_list.Count != 0) {
                return Dig(in_list.Slice(1, in_list.Count - 1), in_sum + in_list[0], in_cat) ||
                       Dig(in_list.Slice(1, in_list.Count - 1), in_sum * in_list[0], in_cat) ||
                       (in_cat && Dig(in_list.Slice(1, in_list.Count - 1), long.Parse(in_sum.ToString() + in_list[0].ToString()), in_cat));
            }
            return in_sum == number_checksum;
        }

        public bool Valid(bool in_cat) {
            return Dig(number_list.Slice(1, number_list.Count - 1), number_list[0], in_cat);
        }
        
        public override string ToString() {
            return $"{number_checksum}, {Tool.StringCollection(number_list)}";
        }
    }
    
    public (ListOp P1, ListOp P2) Prepare(string in_string) {
        var oper_list = new ListOp();
        var string_split = in_string.Split("\n");
        foreach (var temp_line in string_split) {
            var line_split = temp_line.Split(": ");
            var oper_new = new Oper();
            oper_new.number_checksum = long.Parse(line_split[0]);
            oper_new.number_list = line_split[1].Split(" ").Select(long.Parse).ToList();
            oper_list.Add(oper_new);
        }
        return (oper_list, oper_list);
    }

    public long Part1(ListOp in_data) {
        long valid_sum = 0;
        foreach (var temp_oper in in_data) {
            if (temp_oper.Valid(false)) {
                valid_sum += temp_oper.number_checksum;
            }
        }
        return valid_sum;
    }

    public long Part2(ListOp in_data) {
        long valid_sum = 0;
        foreach (var temp_oper in in_data) {
            if (temp_oper.Valid(true)) {
                valid_sum += temp_oper.number_checksum;
            }
        }
        return valid_sum;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day7.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
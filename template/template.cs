namespace aoc2024;

using ReturnAlias = int;
using DayAlias = Day<int, int, int, int>;

public class DayX : DayAlias {

    public (int P1, int P2) Prepare(string in_string) {
        return (0, 0);
    }

    public int Part1(ReturnAlias in_data) {
        return 0;
    }

    public int Part2(ReturnAlias in_data) {
        return 0;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/dayX.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
using System.Text.RegularExpressions;

namespace aoc2024;

public class Day3 : Day<string, string, int, int> {

    public (string P1, string P2) Prepare(string in_string) {
        return (in_string, in_string);
    }

    public int Part1(string in_data) {
        const string regex_pattern = @"mul\((\d+),(\d+)\)";
        var regex_matches = Regex.Matches(in_data, regex_pattern);
        return regex_matches.Sum(temp_match => int.Parse(temp_match.Groups[1].Value) * int.Parse(temp_match.Groups[2].Value));
    }

    public int Part2(string in_data) {
        const string regex_pattern = @"mul\((\d+),(\d+)\)|do\(\)|don't\(\)";
        var regex_matches = Regex.Matches(in_data, regex_pattern);
        var match_toggle = true;
        return regex_matches.Sum(temp_match => {
            switch (temp_match.Value) {
                case "do()":
                    match_toggle = true;
                    break;
                case "don't()":
                    match_toggle = false;
                    break;
                default:
                    if (match_toggle) return int.Parse(temp_match.Groups[1].Value) * int.Parse(temp_match.Groups[2].Value);
                    break;
            }
            return 0;
        });
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day3.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
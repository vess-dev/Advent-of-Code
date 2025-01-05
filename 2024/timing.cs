using System.Diagnostics;

namespace aoc2024;

internal static class Timing {
    private const int test_count = 10;

    private static readonly IDay[] DAY_LIST = [
        new Day1(),
        new Day2(),
        new Day3(),
        new Day4(),
        new Day5(),
        new Day6(),
        new Day7(),
        new Day8(),
    ];

    private static void Time(IDay[] in_days, int in_tests) {
        var time_total = new Stopwatch();
        var time_each = new Stopwatch();
        time_total.Start();
        for (int temp_day = 0; temp_day < in_days.Length; temp_day++) {
            var day_actual = temp_day + 1;
            time_each.Start();
            (object, object) day_return = ("none", "none");
            for (int temp_test = 0; temp_test < test_count; temp_test++) {
                 day_return = in_days[temp_day].Run();
            }
            time_each.Stop();
            var item_one = day_return.Item1.ToString();
            var item_two = day_return.Item2.ToString();
            Console.WriteLine($"Day {day_actual}: ({item_one}, {item_two})");
            var elapsed_between = Math.Round(time_each.Elapsed.TotalSeconds / test_count, 7);
            Console.WriteLine($"{test_count} trials of day {day_actual}: {elapsed_between} seconds");
        }
        time_total.Stop();
        var since_startavg = Math.Round(time_total.Elapsed.TotalSeconds / test_count, 7);
        Console.WriteLine();
        Console.WriteLine($"{test_count} trials of all, averages: {since_startavg} seconds.");
    }

    private static void Main(string[] args) {
        if (args.Length == 2) {
            int day_arg = int.Parse(args[1]) - 1;
            Console.WriteLine(DAY_LIST[day_arg].Run());
        } else if (args is [_, "t", _]) {
            int day_arg = int.Parse(args[1]) - 1;
            var one_list = new IDay[] { DAY_LIST[day_arg-1] };
            Time(one_list, test_count);
        } else {
            Time(DAY_LIST, test_count);
        }
    }
}
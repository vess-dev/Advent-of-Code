namespace aoc2024;

using DictPos = Dictionary<(int pox_x, int pos_y), char>;
using DayAlias = Day<Grid, Grid, int, int>;

public class Grid {
    public int pos_x;
    public int pos_y;
    private readonly Dictionary<(int pos_x, int pos_y), char> map_grid = new();
    private readonly Dictionary<char, DictPos> map_chars = new();

    public void Eat(string in_line) {
        in_line.ToCharArray().ToList().ForEach(temp_char => {
           map_grid.Add((pos_x, pos_y), temp_char);
           if (!map_chars.ContainsKey(temp_char)) {
               map_chars.Add(temp_char, new(){{(pos_x, pos_y), temp_char}});
           } else {
               map_chars.TryGetValue(temp_char, out var handle_dict);
               handle_dict?.Add((pos_x, pos_y), temp_char);
           }
           pos_x += 1;
        });
        pos_x = 0;
        pos_y += 1;
    }

    public char? Get((int, int) in_pos) {
        if (map_grid.ContainsKey(in_pos)) {
            return map_grid[in_pos];
        }

        return null;
    }

    public DictPos? GetPoses(char in_char) {
        map_chars.TryGetValue(in_char, out var handle_dict);
        return handle_dict;
    }

    public override string ToString() {
        return $"({pos_x}, {pos_y})\n\n" +
               $"{Tool.StringCollection(map_grid)}\n\n" +
               $"{Tool.StringCollection(map_chars.ToList().Select(temp_dict => 
                   $"{temp_dict.Key}, {Tool.StringCollection(temp_dict.Value)}"))}";
    }
}

public class Day4 : DayAlias {

    public (Grid P1, Grid P2) Prepare(string in_string) {
        var handle_grid = new Grid();
        var string_lines = in_string.Split("\n");
        foreach (var temp_line in string_lines) {
            handle_grid.Eat(temp_line);
        }
        handle_grid.pos_x = string_lines[0].Length;
        handle_grid.pos_y += 1;
        return (handle_grid, handle_grid);
    }

    public int Part1(Grid in_data) {
        int xmas_count = 0;
        var list_x = in_data.GetPoses('X').Keys.ToList();
        var LIST_MAS = new[] {'M', 'A', 'S'};
        var DIR_LIST = Enumerable.Range(-1, 3)
            .SelectMany(temp_range => Enumerable.Range(-1, 3), (temp_x, temp_y) => (temp_x, temp_y))
            .Where(temp_pair => !(temp_pair.temp_x == 0 && temp_pair.temp_y == 0));
        foreach (var temp_pos in list_x) {
            foreach (var temp_dir in DIR_LIST) {
                var pos_curr = temp_pos;
                foreach (var temp_targ in LIST_MAS) {
                    pos_curr = (pos_curr.pox_x + temp_dir.temp_x, pos_curr.pos_y + temp_dir.temp_y);
                    var dict_targ = in_data.GetPoses(temp_targ);
                    if (!dict_targ.ContainsKey(pos_curr)) {
                        break;
                    }
                    if (temp_targ == 'S') {
                        xmas_count += 1;
                    }
                }
            }
        }
        return xmas_count;
    }

    public int Part2(Grid in_data) {
        int xmas_count = 0;
        var list_m = in_data.GetPoses('M').Keys.ToList();
        var LIST_AS = new[] {'A', 'S'};
        var DIR_LIST = Enumerable.Range(-1, 3)
            .SelectMany(temp_range => Enumerable.Range(-1, 3), (temp_x, temp_y) => (temp_x, temp_y))
            .Where(temp_pair => !(temp_pair.temp_x == 0 || temp_pair.temp_y == 0));
        var CHECK_DICT = new Dictionary<(int, int), List<(int, int)>>(){
            {(-1, -1), [(-2, 0), (0, -2)]},
            {(-1, 1), [(-2, 0), (0, 2)]},
            {(1, -1), [(0, -2), (2, 0)]},
            {(1, 1), [(0, 2), (2, 0)]},
        };
        foreach (var temp_pos in list_m) {
            foreach (var temp_dir in DIR_LIST) {
                var pos_curr = temp_pos;
                foreach (var temp_targ in LIST_AS) {
                    pos_curr = Tool.SumPair(pos_curr, temp_dir);
                    var dict_targ = in_data.GetPoses(temp_targ);
                    if (!dict_targ.ContainsKey(pos_curr)) {
                        break;
                    }
                    if (temp_targ == 'S') {
                        CHECK_DICT.TryGetValue(temp_dir, out var handle_list);
                        var check_one = Tool.SumPair(temp_pos, handle_list[0]);
                        var check_two = Tool.SumPair(temp_pos, handle_list[1]);
                        if (in_data.Get(check_one) == 'M' && in_data.Get(check_two) == 'S') {
                            xmas_count += 1;
                        }
                        if (in_data.Get(check_one) == 'S' && in_data.Get(check_two) == 'M') {
                            xmas_count += 1;
                        }
                    }
                }
            }
        }
        return xmas_count / 2;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day4.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
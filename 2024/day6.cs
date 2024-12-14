namespace aoc2024;

public class Day6 : Day<Day6.Grid, Day6.Grid, int, int> {
    
    public class Grid {
        public (int pos_x, int pos_y) pos_curr = (0, 0);
        public (int pos_x, int pos_y) pos_guard = (0, 0);
        public Dictionary<(int pos_x, int pos_y), char> map_grid = new();
        public Dictionary<(int pos_x, int pos_y), int> map_walked = new();
        private readonly Dictionary<char, (int pos_x, int pos_y)> DIR_DICT = new() {
            {'^', (0, -1)},
            {'>', (1, 0)},
            {'v', (0, 1)},
            {'<', (-1, 0)},
        };
        private readonly Dictionary<char, char> DIR_NEXT = new() {
            {'^', '>'},
            {'>', 'v'},
            {'v', '<'},
            {'<', '^'},
        };

        public void Eat(string in_line) {
            in_line.ToCharArray().ToList().ForEach(temp_char => {
                map_grid.Add(pos_curr, temp_char);
                if (temp_char == '^') {
                    pos_guard.pos_x = pos_curr.pos_x;
                    pos_guard.pos_y = pos_curr.pos_y;
                }
                pos_curr.pos_x += 1;
            });
            pos_curr.pos_x = 0;
            pos_curr.pos_y += 1;
        }
        
        public char? Get((int, int) in_pos) {
            if (map_grid.ContainsKey(in_pos)) {
                return map_grid[in_pos];
            }
            return null;
        }
        
        public void Set((int, int) in_pos, char in_char) {
            map_grid[in_pos] = in_char;
        }

        public bool Walk(bool in_loop) {
            while (true) {
                map_grid.TryGetValue(pos_guard, out var guard_curr);
                var guard_dir = DIR_DICT[guard_curr];
                var next_pos = Tool.SumPair(pos_guard, guard_dir);
                map_grid.TryGetValue(next_pos, out var next_char);
                if (next_char == '#') {
                    map_grid[pos_guard] = DIR_NEXT[guard_curr];
                } else if (next_char == '.') {
                    map_grid[pos_guard] = '.';
                    map_grid[next_pos] = guard_curr;
                    pos_guard = next_pos;
                    if (!map_walked.ContainsKey(next_pos)) {
                        map_walked.Add(next_pos, 1);
                    }
                    else {
                        map_walked[next_pos]++;
                        if (in_loop) {
                            if (map_walked[next_pos] == 4) {
                                return true;
                            }
                        }
                    }
                }
                else {
                    return false;
                }
            }
        }

        public Grid Clone() {
            var handle_grid = new Grid();
            handle_grid.pos_guard = (pos_guard.pos_x, pos_guard.pos_y);
            handle_grid.pos_curr = (pos_curr.pos_x, pos_curr.pos_y);
            handle_grid.map_grid = new(map_grid);
            handle_grid.map_walked = new(map_walked);
            return handle_grid;
        }
    }

    public (Grid P1, Grid P2) Prepare(string in_string) {
        var handle_grid = new Grid();
        var string_lines = in_string.Split("\n");
        foreach (var temp_line in string_lines) {
            handle_grid.Eat(temp_line);
        }
        handle_grid.pos_curr.pos_x = string_lines[0].Length;
        handle_grid.map_walked.Add(handle_grid.pos_guard, 1);
        return (handle_grid, handle_grid.Clone());
    }

    public int Part1(Grid in_data) {
        in_data.Walk(false);
        return in_data.map_walked.Count;
    }

    public int Part2(Grid in_data) {
        var loop_count = 0;
        var test_grid = in_data.Clone();
        test_grid.Walk(false);
        foreach (var temp_pos in test_grid.map_walked.Keys) {
            if (in_data.map_grid[temp_pos] != '#' && in_data.map_grid[temp_pos] != '^') {
                var grid_new = in_data.Clone();
                grid_new.map_grid[temp_pos] = '#';
                if (grid_new.Walk(true)) {
                    loop_count++;
                }
            }
        }
        return loop_count;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day6.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
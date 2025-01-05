namespace aoc2024;

public class Day8 : Day<Day8.Board, Day8.Board, int, int> {

    public class Board {
        public (int pos_x, int pos_y) pos_curr = (0, 0);
        public (int pos_x, int pos_y) pos_size = (0, 0);
        public Dictionary<char, List<(int, int)>> map_grid = new();

        public void Eat(string in_line) {
            in_line.ToCharArray().ToList().ForEach(temp_char => {
                if (temp_char != '.') {
                    if (map_grid.ContainsKey(temp_char)) {
                        map_grid.TryGetValue(temp_char, out var handle_list);
                        handle_list!.Add(pos_curr);
                    } else {
                        map_grid.Add(temp_char, new List<(int, int)> {pos_curr});
                    }
                }
                pos_curr.pos_x += 1;
            });
            pos_curr.pos_x = 0;
            pos_curr.pos_y += 1;
        }
    }

    public (Board P1, Board P2) Prepare(string in_string) {
        var handle_grid = new Board();
        var string_split = in_string.Split("\n");
        foreach (var temp_line in string_split) {
            handle_grid.Eat(temp_line);
            handle_grid.pos_size.pos_x = temp_line.Length;
        }
        handle_grid.pos_size.pos_y = handle_grid.pos_curr.pos_y;
        return (handle_grid, handle_grid);
    }
    
    public int Part1(Board in_data) {
        var unique_nodes = new HashSet<(int, int)>();
        foreach (var temp_list in in_data.map_grid.Values) {
            foreach (var temp_pos in temp_list) {
                foreach (var temp_comp in temp_list) {
                    if (temp_pos != temp_comp) {
                        int new_x = (temp_pos.Item1 - temp_comp.Item1) + temp_pos.Item1;
                        int new_y = (temp_pos.Item2 - temp_comp.Item2) + temp_pos.Item2;
                        if (Tool.InBounds((new_x, new_y), 0, in_data.pos_size.pos_x - 1)) {
                            unique_nodes.Add((new_x, new_y));
                        }
                    }
                }
            }
        }
        return unique_nodes.Count();
    }

    public int Part2(Board in_data) {
        var unique_nodes = new HashSet<(int, int)>();
        foreach (var temp_list in in_data.map_grid.Values) {
            foreach (var temp_pos in temp_list) {
                foreach (var temp_comp in temp_list) {
                    if (temp_pos != temp_comp) {
                        unique_nodes.Add(temp_pos);
                        int new_x = (temp_pos.Item1 - temp_comp.Item1) + temp_pos.Item1;
                        int new_y = (temp_pos.Item2 - temp_comp.Item2) + temp_pos.Item2;
                        while (Tool.InBounds((new_x, new_y), 0, in_data.pos_size.pos_x - 1)) {
                            unique_nodes.Add((new_x, new_y));
                            new_x += (temp_pos.Item1 - temp_comp.Item1);
                            new_y += (temp_pos.Item2 - temp_comp.Item2);
                        }
                    }
                }
            }
        }
        return unique_nodes.Count();
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day8.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
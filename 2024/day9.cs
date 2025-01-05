namespace aoc2024;

public class Day9 : Day<List<int>, List<(int, int)>, long, long> {

    public List<int> Diskify(string in_string) {
        List<int> handle_disk = new();
        bool toggle_pad = false;
        int file_id = 0;
        in_string.ToList().ForEach(temp_char => {
            int char_parse = int.Parse(temp_char.ToString());
            if (!toggle_pad) {
                for (int temp_idx = 0; temp_idx < char_parse; temp_idx++) {
                    handle_disk.Add(file_id);
                }
                file_id += 1;
            } else {
                for (int temp_idx = 0; temp_idx < char_parse; temp_idx++) {
                    handle_disk.Add(-1);
                }
            }
            toggle_pad = !toggle_pad;
        });
        return handle_disk;
    }

    public List<(int, int)> Drivify(string in_string) {
        List<(int, int)> handle_drive = new();
        bool toggle_pad = false;
        int file_id = 0;
        in_string.ToList().ForEach(temp_char => {
            int char_parse = int.Parse(temp_char.ToString());
            if (!toggle_pad) {
                handle_drive.Add((file_id, char_parse));
                file_id += 1;
            } else {
                handle_drive.Add((-1, char_parse));
            }
            toggle_pad = !toggle_pad;
        });
        return handle_drive;
    }

    public (List<int> P1, List<(int, int)> P2) Prepare(string in_string) {
        List<int> handle_disk1 = Diskify(in_string);
        List<(int, int)> handle_disk2 = Drivify(in_string);
        return (handle_disk1, handle_disk2);
    }

    public long Score(List<int> in_data) {
        long check_sum = 0;
        for (int temp_idx = 0; temp_idx < in_data.Count; temp_idx++) {
            if (in_data[temp_idx] == -1) {
                continue;
            }
            check_sum += in_data[temp_idx] * temp_idx;
        }
        return check_sum;
    }

    public long Part1(List<int> in_data) {
        int last_idx = in_data.Count - 1;
        for (int temp_idx = 0; temp_idx < last_idx; temp_idx++) {
            if (in_data[temp_idx] == -1) {
                while (in_data[last_idx] == -1) {
                    last_idx--;
                }
                in_data[temp_idx] = in_data[last_idx];
                in_data[last_idx] = -1;
                last_idx--;
            }
        }
        return Score(in_data);
    }

    public long Part2(List<(int, int)> in_data) {
        for (int temp_idx = 0; temp_idx < in_data.Count; temp_idx++) {
            if (in_data[temp_idx].Item1 == -1) {
                for (int temp_pos = in_data.Count - 1; temp_pos > temp_idx; temp_pos--) {
                    if (in_data[temp_pos].Item1 != -1 && in_data[temp_pos].Item2 <= in_data[temp_idx].Item2) {
                        in_data.Insert(temp_idx, in_data[temp_pos]);
                        in_data[temp_pos + 1] = (-1, in_data[temp_pos + 1].Item2);
                        var handle_old = in_data[temp_idx + 1];
                        handle_old.Item2 -= in_data[temp_idx].Item2;
                        if (handle_old.Item2 == 0) {
                            in_data.RemoveAt(temp_idx + 1);
                        } else {
                            in_data[temp_idx + 1] = handle_old;
                        }
                        break;
                    }
                }
            }
        }
        List<int> handle_disk = new();
        foreach (var temp_pair in in_data) {
            for (int temp_itr = 0; temp_itr < temp_pair.Item2; temp_itr++) {
                handle_disk.Add(temp_pair.Item1);
            }
        }
        return Score(handle_disk);
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day9.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
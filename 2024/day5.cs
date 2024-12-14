namespace aoc2024;

using DayAlias = Day<Printer, Printer, int, int>;

public class Order {
    public List<int> page_list = new();
    public int page_mid;
    public Dictionary<int, int> page_pos = new();
    
    public override string ToString() {
        return $"{page_mid}, {Tool.StringCollection(page_list)}, {Tool.StringCollection(page_pos)}";
    }
}

public class Printer {
    public readonly Dictionary<int, List<int>> rule_dict = new();
    public readonly List<Order> order_list = new();

    public void AddRule(int in_before, int in_after) {
        if (!rule_dict.ContainsKey(in_before)) {
            rule_dict.Add(in_before, new(){in_after});
        } else {
            rule_dict.TryGetValue(in_before, out var handle_list);
            handle_list?.Add(in_after);
        }
    }

    private Dictionary<int, int> GenDict(List<int> in_list) {
        return in_list.Select((temp_order, temp_index) => new {temp_order, temp_index})
            .ToDictionary(temp_pair => temp_pair.temp_order, temp_pair => temp_pair.temp_index);
    }

    public void AddOrder(List<int> in_list) {
        var order_new = new Order();
        order_new.page_list = in_list;
        order_new.page_mid = in_list[in_list.Count/2];
        order_new.page_pos = GenDict(in_list);
        order_list.Add(order_new);
    }

    public bool CheckOrder(Order in_order) {
        return in_order.page_list.All(temp_page => {
            in_order.page_pos.TryGetValue(temp_page, out var page_index);
            rule_dict.TryGetValue(temp_page, out var handle_rules);
            return handle_rules?.All(temp_target => {
                if (in_order.page_pos.ContainsKey(temp_target)) {
                    in_order.page_pos.TryGetValue(temp_target, out var page_check);
                    return page_index <= page_check;
                }
                return true;
            }) ?? true;
        });
    }
    
    public void FixOrder(Order in_order) {
        foreach (var temp_page in in_order.page_list) {
            in_order.page_pos.TryGetValue(temp_page, out var page_index);
            rule_dict.TryGetValue(temp_page, out var handle_rules);
            if (handle_rules != null) {
                foreach (var temp_target in handle_rules) {
                    if (in_order.page_list.Contains(temp_target)) {
                        in_order.page_pos.TryGetValue(temp_target, out var page_check);
                        if (page_index > page_check) {
                            in_order.page_list.RemoveAt(page_index);
                            in_order.page_list.Insert(page_check, temp_page);
                            in_order.page_pos = GenDict(in_order.page_list);
                            in_order.page_mid = in_order.page_list[in_order.page_list.Count/2];
                            return;
                        }
                    }
                }
            }
        }
    }
    
    public override string ToString() {
        return $"{Tool.StringCollection(rule_dict.ToList().Select(temp_pair => $"{temp_pair.Key}, {Tool.StringCollection(temp_pair.Value)}\n"))}" +
               $"{Tool.StringCollection(order_list.Select(temp_order => $"{temp_order}, \n"))}";
    }
}

public class Day5 : DayAlias {

    public (Printer P1, Printer P2) Prepare(string in_string) {
        var handle_printer = new Printer();
        var string_split = in_string.Split("\n\n");
        var rule_split = string_split[0].Split("\n");
        var order_split = string_split[1].Split("\n");
        foreach (var temp_rule in rule_split) {
            var rule_pair = temp_rule.Split("|");
            handle_printer.AddRule(int.Parse(rule_pair[0]), int.Parse(rule_pair[1]));
        }
        foreach (var temp_order in order_split) {
            var order_list = temp_order.Split(",").Select(int.Parse).ToList();
            handle_printer.AddOrder(order_list);
        }
        return (handle_printer, handle_printer);
    }

    public int Part1(Printer in_data) {
        int page_mids = 0;
        foreach (var temp_order in in_data.order_list) {
            if (in_data.CheckOrder(temp_order)) {
                page_mids += temp_order.page_mid;
            }
        }
        return page_mids;
    }

    public int Part2(Printer in_data) {
        int page_mids = 0;
        foreach (var temp_order in in_data.order_list) {
            if (!in_data.CheckOrder(temp_order)) {
                in_data.FixOrder(temp_order);
                while (!in_data.CheckOrder(temp_order)) {
                    in_data.FixOrder(temp_order);
                }
                page_mids += temp_order.page_mid;
            }
        }
        return page_mids;
    }

    public (object P1, object P2) Run() {
        var input_raw = File.ReadAllText("input/day5.txt");
        var input_clean = Prepare(input_raw);
        return (Part1(input_clean.P1), Part2(input_clean.P2));
    }
}
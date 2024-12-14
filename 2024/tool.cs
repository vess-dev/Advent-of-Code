namespace aoc2024;

public static class Tool {

    public static (int, int) SumPair((int, int) in_one, (int, int) in_two) {
        return (in_one.Item1 + in_two.Item1, in_one.Item2 + in_two.Item2);
    }
    
    public static IEnumerable<T> Cycle<T>(IEnumerable<T> in_items) {
        while (true) {
            foreach (var temp_item in in_items) {
                yield return temp_item;
            }
        }
    }

    public static void InspectCollections<T>(params IEnumerable<T>[] in_collections) {
        foreach (var temp_collection in in_collections) {
            Console.WriteLine($"[{String.Join(", ", temp_collection)}]");
        }
    }

    public static string StringCollection<T>(IEnumerable<T> in_collection) {
        return $"[{String.Join(", ", in_collection)}]";
    }

    public static bool Between(this int in_num, int in_min, int in_max) {
        if (in_num < in_min) return false;
        return !(in_num > in_max);
    }
    
}
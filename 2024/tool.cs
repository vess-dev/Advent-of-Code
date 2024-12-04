namespace aoc2024;

public static class Tool {

    public static void InspectCollections<T>(params IEnumerable<T>[] in_collections) {
        foreach (var temp_collection in in_collections) {
            Console.WriteLine($"[{String.Join(", ", temp_collection)}]");
        }
    }

    public static bool Between(this int in_num, int in_min, int in_max) {
        if (in_num < in_min) return false;
        return !(in_num > in_max);
    }
    
}
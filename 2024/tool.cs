namespace aoc2024;

public static class Tool {
    
    public static string LoadFile(string in_path) {
        return File.ReadAllText(in_path);
    }

    public static void InspectCollection<T>(IEnumerable<T> in_collection) {
        Console.WriteLine($"[{String.Join(", ", in_collection)}]");
    }
    
}
namespace aoc2024;

public interface IDay {
    public (object, object) Run();
}

public interface Day<I1, I2, O1, O2> : IDay {
    public (I1, I2) Prepare(string in_string);
    public O1 Part1(I1 in_data);
    public O2 Part2(I2 in_data);
}
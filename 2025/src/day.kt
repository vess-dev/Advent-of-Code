typealias DayReturn = Pair<Any, Any>

public interface IDay {
	fun run(): DayReturn
}

public interface Day<I1, I2, O1, O2> : IDay {
	fun prepare(inString: String): Pair<I1, I2>
	fun part1(inData: I1): O1
	fun part2(inData: I2): O2
}
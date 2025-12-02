internal typealias InputX = Any
internal typealias OutputX = Any

class DayX: Day<InputX, InputX, OutputX, OutputX> {

	override fun prepare(inString: String): Pair<InputX, InputX> {
		return Pair(0, 0)
	}

	override fun part1(inData: InputX): OutputX {
		return 0
	}

	override fun part2(inData: InputX): OutputX {
		return 0
	}

	override fun run(): Pair<OutputX, OutputX> {
		val inputRaw = tool.readInput("dayX")
		val inputClean = prepare(inputRaw)
		return Pair(part1(inputClean.first), part2(inputClean.second))
	}
}
typealias Input = Any
typealias Output = Any

class day1: Day<Input, Input, Output, Output> {

	override fun prepare(inString: String): Pair<Input, Input> {
		return Pair(0, 0)
	}

	override fun part1(inData: Input): Output {
		return 0
	}

	override fun part2(inData: Input): Output {
		return 0
	}

	override fun run(): Pair<Output, Output> {
		val inputRaw = tool.readInput("dayX")
		val inputClean = prepare(inputRaw)
		return Pair(part1(inputClean.first), part2(inputClean.second))
	}
}
private typealias Input4 = Grid
private typealias Output4 = Int

class Day4: Day<Input4, Input4, Output4, Output4> {

    override fun prepare(inString: String): Pair<Input4, Input4> {
        val gridHandle = Grid(inString.length)
        inString.split("\n").forEachIndexed { yPos, string -> string.toCharArray().forEachIndexed {
            xPos, char -> if (char != '.') gridHandle.add(Point(xPos, yPos), char)
        } }
        return Pair(gridHandle, gridHandle)
    }

    override fun part1(inData: Input4): Output4 {
        return inData.keys().sumOf { point -> if (inData.getNearby(point).size < 4) 1 else 0 }
    }

    override fun part2(inData: Input4): Output4 {
        var paperRemoved = 0
        while (inData.keys().any { point -> inData.getNearby(point).size < 4 }) {
            inData.keys().mapNotNull { point -> if (inData.getNearby(point).size < 4) point else null }
                .forEach { point -> inData.remove(point); paperRemoved += 1 }
        }
        return paperRemoved
    }

    override fun run(): Pair<Output4, Output4> {
        val inputRaw = Tool.readInput("day4")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
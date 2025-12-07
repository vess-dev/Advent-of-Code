private typealias Input2 = List<Day2.Range>
private typealias Output2 = Long

class Day2: Day<Input2, Input2, Output2, Output2> {

    class Range(val start: Long, val end: Long)

    override fun prepare(inString: String): Pair<Input2, Input2> {
        val rangeList = inString.split(",")
            .map { range -> range.split("-")
                .map { it.toLong() } }
            .map { array -> Range(array[0], array[1]) }
            .toList()
        return Pair(rangeList, rangeList)
    }

    fun palindrome(inRange: Range): Long {
        return (inRange.start..inRange.end)
            .sumOf { number ->
                val string = number.toString()
                if (string.take(string.length / 2) == string.substring(string.length / 2))
                    string.toLong()
                else 0
            }
    }

    override fun part1(inData: Input2): Output2 {
        return inData.sumOf { range -> palindrome(range) }
    }

    fun loopy(inRange: Range): Long {
        return (inRange.start..inRange.end)
            .sumOf { number ->
                val string = number.toString()
                if (string.length > 1 && string.count { char -> char == string[0] } == string.length || ((2..(string.length / 2)).reversed().any { length ->
                    string.length % length == 0 && string.split(string.take(length)).size - 1 == (string.length / length)
                })) string.toLong()
                else 0
            }
    }

    override fun part2(inData: Input2): Output2 {
        return inData.sumOf { range -> loopy(range) }
    }

    override fun run(): Pair<Output2, Output2> {
        val inputRaw = Tool.readInput("day2")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
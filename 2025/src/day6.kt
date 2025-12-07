private typealias Input6 = Day6.Blackboard
private typealias Output6 = Long

class Day6: Day<Input6, Input6, Output6, Output6> {

    enum class Op {
        ADD,
        MULT,
    }

    class Blackboard(val numbersLists: List<List<Int>>, val stringsList: List<String>, val ops: List<Op>) {
        fun octopusLists(): List<List<Int>> {
            val finalList = mutableListOf<List<Int>>()
            var nextList = mutableListOf<Int>()
            for (tempIndex in 0..<stringsList[0].length) {
                var numberString = ""
                for (tempCol in 0..<stringsList.size) {
                    numberString += stringsList[tempCol][tempIndex]
                }
                if (numberString.all { char -> char == ' ' }) {
                    finalList.add(nextList)
                    nextList = mutableListOf()
                    continue
                }
                nextList.add(numberString.trim().toInt())
            }
            finalList.add(nextList)
            return finalList
        }
    }

    fun foldBlackboard(inNumbersLists: List<List<Int>>, inOps: List<Op>): Long {
        return inNumbersLists.mapIndexed { index, column ->
            column.fold(0L, { acc, number ->
                if (inOps[index] == Op.ADD) acc + number else (if (acc == 0L) 1 else acc) * number
            }) }.sum()
    }

    override fun prepare(inString: String): Pair<Input6, Input6> {
        val stringSplit = inString.split("\n")
        val rowsStrings = stringSplit.subList(0, stringSplit.size - 1)
        val rowStringsReversed = rowsStrings.map { line -> line.reversed() }
        val rowsBase = rowsStrings.map { line ->
            line.split(" ").mapNotNull { it.toIntOrNull() }
        }
        val columnsInts = rowsBase[0].mapIndexed { index, number ->
            rowsBase.map { row -> row[index] }
        }
        val ops = stringSplit.last().split(" ").map { chunk -> chunk.trim() }.mapNotNull { op -> if (op == "+") Op.ADD else if (op == "*") Op.MULT else null }
        val blackboard = Blackboard(columnsInts, rowStringsReversed, ops)
        return Pair(blackboard, blackboard)
    }

    override fun part1(inData: Input6): Output6 {
        return foldBlackboard(inData.numbersLists, inData.ops)
    }

    override fun part2(inData: Input6): Output6 {
        return foldBlackboard(inData.octopusLists(), inData.ops.reversed())
    }

    override fun run(): Pair<Output6, Output6> {
        val inputRaw = Tool.readInput("day6")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
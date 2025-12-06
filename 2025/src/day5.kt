private typealias Input5 = Pair<Day5.Inventory, List<Long>>
private typealias Output5 = Any

class Day5: Day<Input5, Input5, Output5, Output5> {

    class Range(var min: Long, var max: Long) {
        fun inside(inNumber: Long): Boolean {
            return inNumber in min..max
        }
    }

    class Inventory(val ranges: List<Range>) {
        fun fresh(inList: List<Long>): List<Long> {
            return inList.mapNotNull { id -> if (ranges.any { range -> range.inside(id)}) id else null }
        }
    }

    override fun prepare(inString: String): Pair<Input5, Input5> {
        val stringSplit = inString.split("\n\n")
        val rangeList = stringSplit[0].split("\n").map { line -> val lineSplit = line.split("-"); Range(lineSplit[0].toLong(), lineSplit[1].toLong()) }
        val inventory = Inventory(rangeList)
        val idList = stringSplit[1].split("\n").map { number -> number.toLong() }
        val inventoryListPair = Pair(inventory, idList)
        return Pair(inventoryListPair, inventoryListPair)
    }

    override fun part1(inData: Input5): Output5 {
        return inData.first.fresh(inData.second).size
    }

    override fun part2(inData: Input5): Output5 {
        val rangesRef = inData.first.ranges.sortedBy { range -> range.min }
        var rangeTotal = 0L
        var rangeNew: Range = rangesRef.first()
        for (tempRange in rangesRef) {
            if (tempRange.min > rangeNew.max) {
                rangeTotal += (rangeNew.max - rangeNew.min) + 1
                rangeNew = tempRange
            } else if (tempRange.max > rangeNew.max) {
                rangeNew.max = tempRange.max
            }
        }
        return rangeTotal + (rangeNew.max - rangeNew.min) + 1
    }

    override fun run(): Pair<Output5, Output5> {
        val inputRaw = tool.readInput("day5")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}

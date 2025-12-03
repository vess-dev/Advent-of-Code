import com.github.shiguruikai.combinatoricskt.combinations

private typealias Input3 = List<Day3.Bank>
private typealias Output3 = Long

class Day3: Day<Input3, Input3, Output3, Output3> {

    class Bank(val batteries: List<Int>)

    override fun prepare(inString: String): Pair<Input3, Input3> {
        val bankList = inString.split("\n").map { line -> val intList = line.toList().map { it.toString().toInt() }; Bank(intList) }
        return Pair(bankList, bankList)
    }

    fun maxNumber(inList: List<Int>, size: Int): Long {
        val max = inList.subList(0, inList.size - (size - 1)).max()
        val index = inList.indexOf(max)
        val subList = inList.subList(index + 1, inList.size)
        return (max.toString() + (if (size != 1) maxNumber(subList, size - 1) else "").toString()).toLong()
    }

    override fun part1(inData: Input3): Output3 {
        return inData.sumOf { bank -> maxNumber(bank.batteries, 2) }
    }

    override fun part2(inData: Input3): Output3 {
        return inData.sumOf { bank -> maxNumber(bank.batteries, 12) }
    }

    override fun run(): Pair<Output3, Output3> {
        val inputRaw = tool.readInput("day3")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
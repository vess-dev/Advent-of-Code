import Tool.inspect

private typealias Input10 = List<Day10.Machine>
private typealias Output10 = Any

class Day10: Day<Input10, Input10, Output10, Output10> {

    class Machine(val target: List<Boolean>, val buttons: List<List<Int>>, val joltages: List<Int>)
    
    override fun prepare(inString: String): Pair<Input10, Input10> {
        val machineList = inString.split("\n").map { line ->
            val sectionsList = line.split("] ", " {")
            val targetList = sectionsList[0].drop(1).map { char -> char == '#' }
            val buttonsList = sectionsList[1].split(" ").map { group ->
                group.drop(1).dropLast(1).split(",").map { number -> number.toInt() }
            }
            val joltagesList = sectionsList[2].dropLast(1).split(",").map { number -> number.toInt() }
            Machine(targetList, buttonsList, joltagesList)
        }
        return Pair(machineList, machineList)
    }
    
    private fun pressButtons(target: List<Boolean>, buttons: List<List<Int>>): Int {
        val cacheMap = mutableMapOf<String, List<Boolean>>()
        var treeMap = mutableMapOf<List<List<Int>>, List<Boolean>>(
            Pair(listOf(), List(target.size) { false })
        )
        while (true) {
            val treeMapNext = 
            for (tempTree ) {
                
            }
        }
    }
    
    override fun part1(inData: Input10): Output10 {
        return inData.sumOf { machine -> pressButtons(
            machine.target,
            machine.buttons,
            )}
    }

    override fun part2(inData: Input10): Output10 {
        return 0
    }

    override fun run(): Pair<Output10, Output10> {
        val inputRaw = Tool.readInput("day10")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
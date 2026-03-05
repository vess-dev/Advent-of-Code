import kotlin.math.sqrt

private typealias Input8 = List<Day8.Junction>
private typealias Output8 = Long

class Day8: Day<Input8, Input8, Output8, Output8> {

    class Junction(val x: Long, val y: Long, val z: Long) {
        var id: Int? = null

        override fun toString(): String {
            return "($id: $x, $y, $z)"
        }
    }
    
    override fun prepare(inString: String): Pair<Input8, Input8> {
        val junctionList = inString.split("\n").map { line ->
            val split = line.split(",").map { number -> number.toLong() }
            Junction(split[0], split[1], split[2])
        }.toList()
        return Pair(junctionList, junctionList.map { junc -> Junction(junc.x, junc.y, junc.z) })
    }
    
    private fun circuitDistance(inJunction1: Junction, inJunction2: Junction): Double {
        val x = inJunction2.x - inJunction1.x
        val y = inJunction2.y - inJunction1.y
        val z = inJunction2.z - inJunction1.z
        val sum = (x*x) + (y*y) + (z*z)
        return sqrt(sum.toDouble())
    }
    
    private fun precomputeDistances(inData: Input8): Pair<HashMap<Pair<Junction, Junction>, Double>, List<Pair<Junction, Junction>>> {
        val precomputeMap = HashMap<Pair<Junction, Junction>, Double>()
        for (tempIndex1 in 0..<inData.size - 1) {
            val junction1 = inData[tempIndex1]
            for (tempIndex2 in (tempIndex1 + 1)..<inData.size) {
                val junction2 = inData[tempIndex2]
                val mapKey = Pair(junction1, junction2)
                precomputeMap[mapKey] = circuitDistance(junction1, junction2)
            }
        }
        val precomputeSorted = precomputeMap.keys.sortedBy { pair -> precomputeMap[pair] }
        return Pair(precomputeMap, precomputeSorted)
    }
    
    private fun connectCircuits(inData: Input8, connections: Int, flippyBit: Boolean): Output8 {
        val precomputeTuple = precomputeDistances(inData)
        var circuitId = 0
        var connectedCircuits = 0
        val circuitMap = HashMap<Int, MutableList<Junction>>()
        for (junctionPair in precomputeTuple.second) {
            val first = junctionPair.first
            val second = junctionPair.second
            val firstId = first.id
            val secondId = second.id
            val idsNotEqual = firstId != secondId
            val idsBothNull = firstId == null && secondId == null
            val idsBothNotNull = firstId != null && secondId != null
            if (idsNotEqual || idsBothNull) {
                if (idsBothNotNull) {
                    circuitMap[secondId]!!.forEach { junction -> junction.id = firstId }
                    circuitMap[firstId]!!.addAll(circuitMap[secondId]!!)
                    circuitMap.remove(secondId)
                } else if (!idsBothNull) {
                    if (firstId != null) {
                        second.id = firstId
                        circuitMap[firstId]!!.add(second)
                    } else {
                        first.id = secondId
                        circuitMap[secondId]!!.add(first)
                    }
                } else {
                    first.id = circuitId
                    second.id = circuitId
                    circuitMap[circuitId] = mutableListOf(first, second)
                    circuitId++
                }
            }
            connectedCircuits++
            if (!flippyBit && connectedCircuits == connections) {
                break
            } else if (flippyBit && circuitMap.any { (key, value) -> value.size == inData.size}) {
                return (junctionPair.first.x * junctionPair.second.x)
            }
        }
        return circuitMap.values.map { junctions -> junctions.size }.sortedDescending().take(3).reduce { acc, i -> acc * i  }.toLong()
    }

    override fun part1(inData: Input8): Output8 {
        return connectCircuits(inData, 1000, false)
    }

    override fun part2(inData: Input8): Output8 {
        return connectCircuits(inData, 0, true)
    }

    override fun run(): Pair<Output8, Output8> {
        val inputRaw = Tool.readInput("day8")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
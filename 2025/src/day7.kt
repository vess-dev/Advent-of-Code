private typealias Input7 = Day7.Beamer
private typealias Output7 = Any

class Day7: Day<Input7, Input7, Output7, Output7> {
    
    class Beam(val pos: Point, var count: Long) {
        fun testAdd(inPoint: Point) = Beam(pos.testAdd(inPoint), count)
        override fun equals(other: Any?): Boolean {
            if (other !is Beam) return false
            return this.pos == other.pos 
        }
    }
    
    class Beamer(val grid: Grid) {
        val start = Beam(grid.find('S').single(), 1)
        val fall = Point(0, 1)
        val fallLeft = Point(-1, fall.yPos)
        val fallRight = Point(1, fall.yPos)
        fun within(inBeam: Beam): Boolean {
            return grid.within(inBeam.pos)
        }
        fun addBeam(inBeam: Beam, inList: MutableList<Beam>) {
            val beam = inList.find { beam -> beam == inBeam }
            if (beam == null) inList.add(inBeam)
            else beam.count += inBeam.count
        }
        fun beamin(inTimeline: Boolean): Long {
            var beams = listOf(start.testAdd(fall))
            var splits = 0L
            while (true) {
                val newBeams = mutableListOf<Beam>()
                for (tempBeam in beams) {
                    val projectedBeam = tempBeam.testAdd(fall)
                    if (within(projectedBeam)) {
                        val projectedChar = grid.get(projectedBeam.pos)
                        if (projectedChar == '^') {
                            splits += 1
                            val leftBeam = tempBeam.testAdd(fallLeft)
                            addBeam(leftBeam, newBeams)
                            val rightBeam = tempBeam.testAdd(fallRight)
                            addBeam(rightBeam, newBeams)
                        } else {
                            addBeam(projectedBeam, newBeams)
                        }
                    }
                }
                if (newBeams.isEmpty()) break
                beams = newBeams
            }
            return if (!inTimeline) splits else beams.sumOf { beam -> beam.count }
        }
    }
    
    override fun prepare(inString: String): Pair<Input7, Input7> {
        val gridWidth = inString.filter { char -> char == '\n' }.length
        val handleGrid = Grid(gridWidth * gridWidth)
        val validMap = hashMapOf(('S' to true), ('^' to true))
        inString.split("\n").mapIndexed { yPos, line -> line.toList().mapIndexed { xPos, char ->
            if (validMap.containsKey(char)) {
                val point = Point(xPos, yPos)
                handleGrid.add(point, char)
            }
        } }
        val handleBeamer = Beamer(handleGrid)
        return Pair(handleBeamer, handleBeamer)
    }

    override fun part1(inData: Input7): Output7 {
        return inData.beamin(false)
    }

    override fun part2(inData: Input7): Output7 {
        return inData.beamin(true)
    }

    override fun run(): Pair<Output7, Output7> {
        val inputRaw = Tool.readInput("day7")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
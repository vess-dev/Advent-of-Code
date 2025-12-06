import java.io.File
import kotlin.math.abs
import kotlin.math.log10

object tool {
	const val PREPEND = "input/"
	fun readInput(inName: String): String {
		val pathFull = "$PREPEND$inName.txt"
		return File(pathFull).readText()
	}
}

public typealias Point = Pair<Int, Int>

fun Point.add(inPoint: Point): Point {
    return Point(this.first + inPoint.first, this.second + inPoint.second)
}

class Grid(size: Int = 0) {
    var grid = HashMap<Point, Char>(size)
    val relative = listOf(
        Point(-1, -1),
        Point(0, -1),
        Point(1, -1),
        Point(-1, 0),
        Point(1, 0),
        Point(-1, 1),
        Point(0, 1),
        Point(1, 1),
    )
    fun add(inPoint: Point, inChar: Char) {
        grid[inPoint] = inChar
    }
    fun remove(inPoint: Point) {
        grid.remove(inPoint)
    }
    fun get(inPoint: Point): Char? {
        return grid.get(inPoint)
    }
    fun getNearby(inPoint: Point): List<Char> {
        return relative.mapNotNull { offset -> get(inPoint.add(offset)) }
    }
    fun keys(): Set<Point> {
        return grid.keys
    }
}

fun Int.length() = when(this) {
    0 -> 1
    else -> log10(abs(toDouble())).toInt() + 1
}
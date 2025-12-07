import java.io.File
import java.util.Objects
import kotlin.math.abs
import kotlin.math.log10
import kotlin.math.sqrt

object Tool {
	const val PREPEND = "input/"
	fun readInput(inName: String): String {
		val pathFull = "$PREPEND$inName.txt"
		return File(pathFull).readText()
	}
}

class Point(var xPos: Int = 0, var yPos: Int = 0) {
    fun add(inPoint: Point) {
        this.xPos += inPoint.xPos
        this.yPos += inPoint.yPos
    }
    fun testAdd(inPoint: Point): Point {
        return Point(this.xPos + inPoint.xPos, this.yPos + inPoint.yPos)
    }
    fun incX(inXAdd: Int = 1) {
        this.xPos += inXAdd
    }
    fun incY(inYAdd: Int = 1) {
        this.yPos += inYAdd
    }
    fun decX(inXDec: Int = 1) {
        this.xPos -= inXDec
    }
    fun decY(inYDec: Int = 1) {
        this.yPos -= inYDec
    }
    override fun toString(): String {
        return "($xPos,$yPos)"
    }
    override fun equals(other: Any?): Boolean {
        if (other !is Point) return false
        return this.xPos == other.xPos && this.yPos == other.yPos
    }
    override fun hashCode(): Int {
        return Objects.hash(xPos, yPos)
    }
}

class Grid(val inSize: Int = 0, val grid: HashMap<Point, Char> = HashMap(inSize)) {
    private val relative = listOf(
        Point(-1, -1),
        Point(0, -1),
        Point(1, -1),
        Point(-1, 0),
        Point(1, 0),
        Point(-1, 1),
        Point(0, 1),
        Point(1, 1),
    )
    private val sqrt = sqrt(inSize.toDouble()).toInt()
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
        return relative.mapNotNull { offset -> get(inPoint.testAdd(offset)) }
    }
    fun keys(): Set<Point> {
        return grid.keys
    }
    fun find(inChar: Char): Set<Point> {
        return grid.filterValues { char -> char == inChar }.keys
    }
    fun within(inPoint: Point): Boolean {
        return 0 <= inPoint.xPos && 0 <= inPoint.yPos && inPoint.xPos < sqrt && inPoint.yPos < sqrt
    }
}

fun Int.length() = when(this) {
    0 -> 1
    else -> log10(abs(toDouble())).toInt() + 1
}
import Tool.Point
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.async
import kotlinx.coroutines.awaitAll
import kotlinx.coroutines.runBlocking
import kotlin.collections.plus
import kotlin.math.abs
import java.awt.Shape
import java.awt.geom.Path2D

private typealias Input9 = List<Point>
private typealias Output9 = Long

private typealias PointList = List<Point>
private typealias Line = Pair<Point, Point>
private typealias LineList = List<Line>

class Day9: Day<Input9, Input9, Output9, Output9> {
    override fun prepare(inString: String): Pair<Input9, Input9> {
        val pointList = inString.split("\n").map { line ->
            val cords = line.split(",").map { num -> num.toInt() }
            Point(cords[0], cords[1])
        }
        return Pair(pointList, pointList)
    }
    
    private fun area(inOne: Point, inTwo: Point): Long {
        val partOne = abs(inOne.xPos - inTwo.xPos) + 1
        val partTwo = abs(inOne.yPos - inTwo.yPos) + 1
        return partOne.toLong() * partTwo.toLong()
    }
    
    override fun part1(inData: Input9): Output9 {
        return inData.flatMapIndexed { index, point1 -> inData.subList(index + 1, inData.size)
            .map { point2 -> Pair(point1, point2) }
        }.maxOf { pair -> area(pair.first, pair.second) }
    }
    
    private fun generatePoints(inOne: Point, inTwo: Point): PointList {
        val otherX = Point(inOne.xPos, inTwo.yPos)
        val otherY = Point(inTwo.xPos, inOne.yPos)
        return listOf(inOne, otherY, inTwo, otherX)
    }
    
    private fun generateLines(inList: PointList): LineList {
        val wrapList = inList + inList[0]
        return wrapList.subList(0, wrapList.size - 1).mapIndexed { index, point -> 
            Pair(point, wrapList[index + 1])
        }
    }
    
    private fun mapToShape(inMapPoints: PointList): Shape {
        val first = inMapPoints.first()
        val path = Path2D.Double()
        path.moveTo(first.xPos.toDouble(), first.yPos.toDouble())
        for (tempPoint in inMapPoints.subList(1, inMapPoints.size)) {
            path.lineTo(tempPoint.xPos.toDouble(), tempPoint.yPos.toDouble())
        }
        path.closePath()
        return path
    }
    
    private fun isInsideShape(inX: Point, inY: Point, inShape: Shape, inSamples: Int): Boolean {
        val rectPoints = generatePoints(inX, inY)
        val rectLines = generateLines(rectPoints)
        var filteredRectLines = rectLines.filter { line -> line.first != line.second }
        if (filteredRectLines.size == 2) {
            filteredRectLines = filteredRectLines.subList(0, 1)
        }
        return filteredRectLines.all { line ->
            val deltaX = (line.second.xPos - line.first.xPos) / inSamples
            val deltaY = (line.second.yPos - line.first.yPos) / inSamples
            (0..inSamples).all { step ->
                val checkX = line.first.xPos + (deltaX * step)
                val checkY = line.first.yPos + (deltaY * step)
                inShape.intersects(checkX.toDouble() - 0.1, checkY.toDouble() - 0.1, 0.2, 0.2)
            }
        }
    }
    
    override fun part2(inData: Input9): Output9 {
        val mapShape = mapToShape(inData)
        return runBlocking {
            inData.flatMapIndexed { index, point1 ->
                inData.subList(index + 1, inData.size).map { point2 ->
                    async(Dispatchers.Default) {
                        if (isInsideShape(point1, point2, mapShape, 43)) Pair(point1, point2) else null
                    }
                }
            }.awaitAll().filterNotNull()
        }.maxOf { pair -> area(pair.first, pair.second) }
    }

    override fun run(): Pair<Output9, Output9> {
        val inputRaw = Tool.readInput("day9")
        val inputClean = prepare(inputRaw)
        return Pair(part1(inputClean.first), part2(inputClean.second))
    }
}
import Day1.Dir
import kotlin.math.absoluteValue

private typealias Input1 = List<Dir>
private typealias Output1 = Int

class Day1: Day<Input1, Input1, Output1, Output1> {

    sealed class Dir {
		data class Left(val distance: Int) : Dir()
		data class Right(val distance: Int) : Dir()
	}

	class Lock {
		var current = 50
		var zeros = 0
		val max = 100

		fun step(direction: Dir): Int {
			when (direction) {
				is Dir.Left -> modify(-direction.distance)
				is Dir.Right -> modify(direction.distance)
			}
			return current
		}

		fun modify(distance: Int) {
			val sign = if (distance > 0) 1 else -1
			var left = distance.absoluteValue
			while (left > 0) {
				left--
				current = (current + sign).mod(max)
				if (current == 0 && left != 0) zeros++
			}
		}
	}

	override fun prepare(inString: String): Pair<Input1, Input1> {
		val inputSplit = inString.split("\n")
		val inputDirList = inputSplit.map { string ->
			val dialDir = string.first()
			val dialDist = string.substring(1).toInt()
			if (dialDir == 'L') {
				Dir.Left(dialDist)
			} else if (dialDir == 'R') {
				Dir.Right(dialDist)
			} else { null!! }
		}
		return Pair(inputDirList, inputDirList)
	}

	override fun part1(inData: Input1): Output1 {
		val lock = Lock()
		return inData.map { dir -> lock.step(dir) }.count { pos -> pos == 0 }
	}

	override fun part2(inData: Input1): Output1 {
		val lock = Lock()
		return inData.map { dir -> lock.step(dir) }.count { pos -> pos == 0 } + lock.zeros
	}

	override fun run(): Pair<Output1, Output1> {
		val inputRaw = tool.readInput("day1")
		val inputClean = prepare(inputRaw)
		return Pair(part1(inputClean.first), part2(inputClean.second))
	}
}
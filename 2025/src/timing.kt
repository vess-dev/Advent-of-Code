import kotlin.time.Clock
import kotlin.time.DurationUnit
import kotlin.time.ExperimentalTime

@OptIn(ExperimentalTime::class)
fun clock(adventDay: IDay, testCount: Int): Pair<DayReturn, Double> {
	var timeTotal = 0.0
	var testReturn: DayReturn? = null
	for (tempStep in 1..testCount) {
		val timeBefore = Clock.System.now()
		testReturn = adventDay.run()
		timeTotal += Clock.System.now().minus(timeBefore).toDouble(DurationUnit.SECONDS)
	}
	return Pair(testReturn!!, timeTotal)
}

fun main() {
	val adventList = listOf(Day1())
	val testCount: Int? = 1
	var timeTotal = 0.0
	if (testCount != null) {
		for ((tempIndex, tempDay) in adventList.withIndex()) {
			val returnPair = clock(tempDay, testCount)
			val dayNum = tempIndex + 1
			println("Day $dayNum: ${returnPair.first}")
			println("$testCount trials of day $dayNum : ${returnPair.second / testCount}")
			timeTotal += returnPair.second
		}
		println("$testCount trials of all, averages: ${timeTotal / testCount}")
	} else {
		for ((tempIndex, tempDay) in adventList.withIndex()) {
			println("Day $tempIndex: ${tempDay.run()}")
		}
	}
}
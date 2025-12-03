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
	val adventList = listOf(Day1(), Day2(), Day3())
    @Suppress("RedundantNullableReturnType", "RedundantSuppression") val testCount: Int? = 1
    @Suppress("RedundantNullableReturnType", "RedundantSuppression") val specific: Int? = null
	var timeTotal = 0.0
	if (testCount != null && specific == null) {
		for ((tempIndex, tempDay) in adventList.withIndex()) {
			val returnPair = clock(tempDay, testCount)
			val dayNum = tempIndex + 1
			println("Day $dayNum: ${returnPair.first}")
			println("$testCount trials of day $dayNum averages: ${"%.7f".format(returnPair.second / testCount)} seconds.")
			timeTotal += returnPair.second
		}
		println("$testCount trials of all averages: ${"%.7f".format(timeTotal / testCount)} seconds.")
	} else {
        if (specific == null) {
            for ((tempIndex, tempDay) in adventList.withIndex()) {
                println("Day $tempIndex: ${tempDay.run()}")
            }
        } else {
            println("Day $specific: ${adventList[specific - 1].run()}}")
        }
	}
}
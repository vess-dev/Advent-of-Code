import java.io.File

object tool {
	const val PREPEND = "input/"
	fun readInput(inName: String): String {
		val pathFull = "$PREPEND$inName.txt"
		return File(pathFull).readText()
	}
}
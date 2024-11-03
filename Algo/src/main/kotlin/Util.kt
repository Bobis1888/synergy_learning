import kotlin.random.Random

fun generateRandomIntArray(size: Int = 10, from: Int = 1, to: Int = 100): Array<Int> {
    return Array(size) { Random.nextInt(from, to) }
}
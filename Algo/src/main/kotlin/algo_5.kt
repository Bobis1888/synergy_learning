/**
 * На улице встретились N друзей.
 * Каждый пожал руку всем остальным друзьям (по одному разу).
 * Сколько рукопожатий было?
 */
fun handshakes(n: Int): Int {

    if (n < 0) {
        throw IllegalArgumentException("Количество друзей должно быть больше 0")
    }

    return n * (n - 1) / 2
}

fun main() {
    println("Введите число друзей:")
    val numberOfFriends = readLine()

    try {

        if (numberOfFriends.isNullOrEmpty()) {
            throw NumberFormatException()
        }

        numberOfFriends.toInt()
    } catch (ignore: NumberFormatException) {
        println("Вы ввели не число =(")
        return
    }

    val totalHandshakes = handshakes(numberOfFriends.toInt())
    println("Количество рукопожатий: $totalHandshakes")
}
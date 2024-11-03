/**
 * Посчитать четные и нечетные цифры введенного натурального
 * числа. Например, если введено число 34560, в нем 3 четные
 * цифры
 * (4, 6 и 0) и 2 нечетные (3 и 5)
 */
fun main() {
    println("Введите число: ")
    val line = readLine() ?: throw IllegalArgumentException("Введите строку")
    val number: Int

    try {
        number = line.toInt()
    } catch (ex: NumberFormatException) {
        println("Вы ввели не число! =(")
        return
    }

    println("Введено число $number")

    var countOddNumber: Int = 0
    var countEvenNumber: Int = 0

    integerToArray(number).forEach {

        if (it % 2 == 0) {
            countEvenNumber++
        } else {
            countOddNumber++
        }
    }

    println("Количество чисел \nчетных: $countEvenNumber\nнечетных : $countOddNumber")
}

fun integerToArray(num: Int): IntArray {
    val digits = mutableListOf<Int>()
    var tempNum = num

    while (tempNum > 0) {
        digits.add(tempNum % 10)
        tempNum /= 10
    }

    digits.reverse()

    return digits.toIntArray()
}
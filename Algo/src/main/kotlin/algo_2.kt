/**
 * В массиве случайных целых чисел поменять местами
 * минимальный и максимальный элементы.
 */
fun main() {
    var array = generateRandomIntArray()
    println("Дан массив ${array.contentToString()}")
    var minIndex = 0
    var maxIndex = 0

    for (i in array.indices) {

        if (array[i] < array[minIndex]) {
            minIndex = i
        } else if (array[i] > array[maxIndex]) {
            maxIndex = i
        }
    }

    val tmp = array[minIndex]
    array[minIndex] = array[maxIndex]
    array[maxIndex] = tmp

    println("Получили массив ${array.contentToString()}")
}
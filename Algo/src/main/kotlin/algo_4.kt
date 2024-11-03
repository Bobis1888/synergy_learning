/**
 * Отсортируйте по возрастанию методом слияния одномерный
 * вещественный массив, заданный случайными числами на
 * промежутке [0; 50]. Выведите на экран исходный и
 * отсортированный массивы.
 *
 */
fun main() {
    var array = generateRandomIntArray(10, 0, 50)
    println("Дан массив ${array.contentToString()}")

    mergeSort(array)

    println("Получили массив ${array.contentToString()}")
}

fun mergeSort(array: Array<Int>) {

    if (array.size <= 1) {
        return
    }

    val middle = array.size / 2
    val left = array.copyOfRange(0, middle)
    val right = array.copyOfRange(middle, array.size)

    mergeSort(left)
    mergeSort(right)

    merge(left, right, array)
}

fun merge(left: Array<Int>, right: Array<Int>, array: Array<Int>) {
    var i = 0
    var j = 0
    var k = 0

    while (i < left.size && j < right.size) {

        if (left[i] <= right[j]) {
            array[k++] = left[i++]
        } else {
            array[k++] = right[j++]

        }
    }

    while (i < left.size) {
        array[k++] = left[i++]
    }

    while (j < right.size) {
        array[k++] = right[j++]
    }
}
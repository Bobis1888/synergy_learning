/**
 * Отсортируйте по убыванию методом пузырька одномерный
 * целочисленный массив, заданный случайными числами на
 * промежутке [-100; 100].
 * Выведите на экран исходный и отсортированный массивы.
 */
fun main() {
    var array = generateRandomIntArray()
    println("Дан массив ${array.contentToString()}")

    bubbleSort(array)

    println("Получили массив ${array.contentToString()}")
}

fun bubbleSort(array: Array<Int>) {
    var n = array.size
    var count = 0

    for (i in 0 until n - 1) {

        for (j in 0 until n - i - 1) {
            count++

            if (array[j] > array[j + 1]) {

                val temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
            }
        }

        // последний элемент встал на свое место
        n--
    }

    println("Count $count")
}
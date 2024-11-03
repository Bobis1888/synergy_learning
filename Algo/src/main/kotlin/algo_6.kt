import java.util.PriorityQueue

/**
 *  Закодируйте любую строку по алгоритму Хаффмана.
 */

data class Node(var char: Char = ' ', var freq: Int = 0, var left: Node? = null, var right: Node? = null) : Comparable<Node> {
    override fun compareTo(other: Node): Int {
        return freq - other.freq
    }
}

fun serialize(text: String): Map<Char, String> {
    val freqMap = mutableMapOf<Char, Int>()

    text.forEach {
        freqMap[it] = freqMap.getOrDefault(it, 0) + 1
    }

    val pq = PriorityQueue<Node>()
    freqMap.forEach {
        (char, freq) -> pq.add(Node(char, freq))
    }

    while (pq.size > 1) {
        val left = pq.poll()
        val right = pq.poll()
        val node = Node(freq = left.freq + right.freq, left = left, right = right)
        pq.add(node)
    }

    val codes = mutableMapOf<Char, String>()
    val root = pq.peek()

    fun traverse(node: Node, code: String = "") {

        if (node.left == null && node.right == null) {
            codes[node.char] = code
        } else {
            traverse(node.left!!, "${code}0")
            traverse(node.right!!, "${code}1")
        }
    }

    traverse(root)

    return codes
}

fun main() {
    var string = "Hello World!"
    println("Дана строка $string")

    val res = serialize(string)

    println("Получили  $res")
}
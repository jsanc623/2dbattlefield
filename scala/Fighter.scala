object Fighter {
    val ID: Int = Math.random().toInt
    val STATE_OK: Int = 1
    val STATE_POISONED: Int = 0
    val STATE_DEAD: Int = -1
    val MAX_HEALTH: Int = 100

    class Fighter(var position: List[Int]) {
        var state: Int = STATE_OK
        var health: Float = MAX_HEALTH

        def health(amount: Double, op: Int = -1): Int = {
            health = health + (amount.toFloat * op)
            health.toInt
        }

        def position(position: List[Int]): List[Int] = {
            this.position = position
            this.position
        }
    }
}

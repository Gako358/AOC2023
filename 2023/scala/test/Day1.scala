package tests

import aoc.dayOne.solvePart1

def testSolvePart1(): Unit = {
  val input = List(
    "1abc2",
    "pqr3stu8vqx",
    "a1b2c3d4e5f",
    "treb7uchet7"
  )
  val result = solvePart1(input)
  assert(result == 142)
  println(s"Test 1 passed: $result")
}

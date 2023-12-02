package aoc
package dayOne

import scala.annotation.tailrec

def solvePart1(input: List[String]): Int =
  // Get the first number and the last number and add them together
  // Then sum the lines together.
  input
    .map(l => s"${l.find(_.isDigit).get}${l.reverse.find(_.isDigit).get}".toInt)
    .sum

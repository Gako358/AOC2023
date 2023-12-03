package aoc
package dayOne

import scala.annotation.tailrec
import scala.util.matching.Regex

def solvePart1(input: List[String]): Int =
  // Get the first number and the last number and add them together
  // Then sum the lines together.
  input
    .map(l => s"${l.find(_.isDigit).get}${l.reverse.find(_.isDigit).get}".toInt)
    .sum

def solvePart2(input: List[String]): Int = {
  val words = Map(
    "one" -> 1,
    "two" -> 2,
    "three" -> 3,
    "four" -> 4,
    "five" -> 5,
    "six" -> 6,
    "seven" -> 7,
    "eight" -> 8,
    "nine" -> 9
  )

  val numRegex: Regex = (words.keys ++ words.values.map(_.toString)).mkString("(?=(", "|", "))").r
  val matches: String => Int = s => words.getOrElse(s, s.toInt)

  val calibrateVal: String => Int = str =>
    numRegex.findAllIn(str).matchData.toSeq.map(_.group(1)) match {
      case digits if digits.isEmpty => 0
      case digits                   => digits.map(matches).sum
    }

  input.map(line => calibrateVal(line)).sum
}

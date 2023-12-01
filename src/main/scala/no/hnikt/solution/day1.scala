package no.hnikt.solution

import scala.io.Source

object Calibration {
  val stringDigitReprs = Map(
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

  val digitReprs = stringDigitReprs ++ (0 to 9).map(i => i.toString -> i)

  def solve(input: String): String = {
    val digitReprRegex = digitReprs.keysIterator.mkString("|").r

    def lineToCoordinates(line: String): Int = {
      val matchesIter = for {
        lineTail <- line.tails
        oneMatch <- digitReprRegex.findPrefixOf(lineTail)
      } yield oneMatch

      val matches = matchesIter.toList
      val firstDigit = digitReprs(matches.head)
      val lastDigit = digitReprs(matches.last)
      s"$firstDigit$lastDigit".toInt
    }

    val result = input.linesIterator
      .map(lineToCoordinates(_))
      .sum
    result.toString()
  }

  def main(args: Array[String]): Unit = {
    val lines = Source
      .fromFile("src/main/scala/no/hnikt/solution/day1.txt")
      .getLines()
      .toList
    val soln = solve(lines.mkString("\n"))
    println(s"Solution: $soln")
  }
}

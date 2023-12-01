package no.hnikt.solution

import scala.io.Source

object Day1 {
  def main(args: Array[String]): Unit = {
    val lines = Source.fromFile("src/main/scala/no/hnikt/solution/day1.txt").getLines().toList
    // val lines = List(
    //   "two1nine",
    //   "eightwothree",
    //   "abcone2threexyz",
    //   "xtwone3four",
    //   "4nineeightseven2",
    //   "zoneight234",
    //   "7pqrstsixteen"
    // )
    val sum = calculateCalibrationSum(lines)
    println(s"The sum of calibration values is: $sum")
  }

  def calculateCalibrationSum(calibrationDocument: List[String]): Int = {
    val numberMap = Map(
      "zero" -> '0',
      "one" -> '1',
      "two" -> '2',
      "three" -> '3',
      "four" -> '4',
      "five" -> '5',
      "six" -> '6',
      "seven" -> '7',
      "eight" -> '8',
      "nine" -> '9'
    )
    val numberPattern = (numberMap.keys.mkString("|") + "|\\d").r
    calibrationDocument.map { line =>
      val numbers = numberPattern.findAllIn(line).toList
      if (numbers.nonEmpty) {
        val firstNumber =
          numberMap.getOrElse(numbers.head, numbers.head.head).asDigit
        val lastNumber =
          numberMap.getOrElse(numbers.last, numbers.last.head).asDigit
        firstNumber * 10 + lastNumber
      } else {
        0
      }
    }.sum
  }
}

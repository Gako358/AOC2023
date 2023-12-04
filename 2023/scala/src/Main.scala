package aoc

import cats.effect.IOApp
import cats.effect.IO

object MainApp extends IOApp.Simple:
  val d1 =
    for
      data <- getNonEmptyLines[IO]("./../resources/day1.txt")
      data2 <- getNonEmptyLines[IO]("./../resources/day2.txt")
      _ <- IO.println(s"Day one, Part 1: ${dayOne.solvePart1(data)}")
      _ <- IO.println(s"Day one, Part 2: ${dayOne.solvePart2(data)}")
      _ <- IO.println(s"Day two, Part 1: ${dayTwo.solvePart1(data2)}")
    yield ()

  override def run: IO[Unit] =
    d1

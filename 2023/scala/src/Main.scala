package aoc

import cats.effect.IOApp
import cats.effect.IO

object MainApp extends IOApp.Simple:
  val d1 =
    for
      data <- getNonEmptyLines[IO]("./../resources/day1.txt")
      _ <- IO.println(s"Day one, Part 1: ${dayOne.solvePart1(data)}")
    yield ()

  override def run: IO[Unit] =
    d1

package aoc
package dayTwo

val inputData = List(
  "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
  "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
  "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
  "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
  "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
)

// Game constrains
val constraint = Map("red" -> 12, "green" -> 13, "blue" -> 14)

def isValidGame(cubes: Map[String, Int]): Boolean =
  cubes.forall { case (color, count) => count <= constraint(color) }

def solvePart1(input: List[String]): Int =
  input.map { line =>
    val cubes = line
      .split(";")
      .map(_.trim)
      .map { cube =>
        val color = cube.split(" ").last
        val count = cube.split(" ").head.toInt
        color -> count
      }
      .toMap

    if isValidGame(cubes) then cubes.values.sum else 0
  }.sum

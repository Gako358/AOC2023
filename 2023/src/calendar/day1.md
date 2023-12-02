# Day 1: Trebuchet?!

## Introduction

Something is wrong with global snow production, and you've been selected to take a look. The Elves have given you a map, marking the top fifty locations that are likely to have problems with stars.

Your task is to restore snow operations by checking all fifty stars by December 25th. Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

## The Problem

The Elves are having trouble reading the values on their calibration document (your puzzle input) as it has been amended by a very young Elf who was excited to show off her art skills. The calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

### Example

For example, consider these lines:

- 1abc2
- pqr3stu8vwx
- a1b2c3d4e5f
- treb7uchet

The calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

### Task

Consider your entire calibration document. What is the sum of all of the calibration values?

## Part Two

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

### Example

For example, consider these lines:

- two1nine
- eightwothree
- abcone2threexyz
- xtwone3four
- 4nineeightseven2
- zoneight234
- 7pqrstsixteen

The calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

### Task

What is the sum of all of the calibration values?
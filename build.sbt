val http4sVersion = "0.23.23"
val tapirVersion = "1.8.2"
val jsoniterScalaVersion = "2.24.1"
val doobieVersion = "1.0.0-RC4"
val munitCEVersion = "2.0.0-M3"
val xtractVersion = "2.3.0"
val munitVersion = "0.7.29"
val catsCoreVersion = "2.10.0"
val catsEffect3Version = "3.5.2"
val fs2Version = "3.9.2"
val logbackVersion = "1.4.11"
val log4catsSlf4jVersion = "2.6.0"
val liquibaseVersion = "4.24.0"
val h2Version = "2.2.224"
val ductapeVersion = "0.1.11"
val sttpClientVersion = "3.9.0"
val circeVersion = "0.14.6"

lazy val rootProject = (project in file(".")).settings(
  name := "aoc2023",
  version := "0.1.0-SNAPSHOT",
  organization := "no.hnikt",
  scalaVersion := "3.3.1",
  scalacOptions ++= Seq("-Xmax-inlines", "100"),
  libraryDependencies ++= Seq(
    "org.scalameta" %% "munit" % munitVersion % Test,
    "org.typelevel" %% "munit-cats-effect" % munitCEVersion % Test,
    "com.h2database" % "h2" % h2Version % Test,
    "com.h2database" % "h2" % h2Version,
    "org.http4s" %% "http4s-ember-client" % http4sVersion,
    "org.http4s" %% "http4s-ember-server" % http4sVersion,
    "org.http4s" %% "http4s-circe" % http4sVersion,
    "org.http4s" %% "http4s-dsl" % http4sVersion,
    "org.http4s" %% "http4s-circe" % http4sVersion,
    "org.tpolecat" %% "doobie-core" % doobieVersion,
    "org.tpolecat" %% "doobie-hikari" % doobieVersion,
    "org.tpolecat" %% "doobie-h2" % doobieVersion,
    "ch.qos.logback" % "logback-classic" % logbackVersion,
    "org.typelevel" %% "log4cats-slf4j" % log4catsSlf4jVersion,
    "org.liquibase" % "liquibase-core" % liquibaseVersion,
    "io.github.arainko" %% "ducktape" % ductapeVersion,
    "com.mysql" % "mysql-connector-j" % "8.1.0",
    "io.circe" %% "circe-parser" % circeVersion,
     // https://mvnrepository.com/artifact/io.circe/circe-core
    "io.circe" %% "circe-core" % circeVersion,
    "io.circe" %% "circe-generic" % circeVersion,

  )
)

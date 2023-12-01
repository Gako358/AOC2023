{
  description = "advent of code 2023";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [
            (self: super: rec {
              jdk = super.graalvm-ce;
              sbt = super.sbt.override {jre = super.graalvm-ce;};
              maven = super.maven.override {
                inherit jdk;
              };
            })
          ];
        };

        phytonInputs = with pkgs; [
          python3
        ];

        jvmInputs = with pkgs; [
          jdk
          maven
          sbt
          coreutils
        ];

        jsInputs = with pkgs; [
          nodejs
        ];

        jvmHook = ''
          JAVA_HOME="${pkgs.jdk}"
        '';
        ghHook = ''
          source ~/.env
        '';
      in {
        devShells.default = pkgs.mkShell {
          name = "aoc-dev-shell";
          buildInputs = jvmInputs ++ jsInputs ++ phytonInputs;
          shellHook = jvmHook + ghHook;
        };
      }
    );
}

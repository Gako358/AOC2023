{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = {
    nixpkgs,
    flake-utils,
    ...
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {
        inherit system;
        overlays = [
          (f: p: {
            sbt = p.sbt.override {
              jre = p.jdk21;
            };
          })
        ];
      };
      jdk = pkgs.jdk21;
    in {
      devShell = let
        generateEditorConfig = pkgs.writeShellScriptBin "generateEditorConfig" ''
          if [ ! -f .editorconfig ]; then
            echo "root = true" > .editorconfig
            echo "" >> .editorconfig
            echo "[*]" >> .editorconfig
            echo "end_of_line = lf" >> .editorconfig
            echo "insert_final_newline = true" >> .editorconfig
            echo "indent_style = space" >> .editorconfig
            echo "tab_width = 4" >> .editorconfig
            echo "charset = utf-8" >> .editorconfig
            echo "" >> .editorconfig
            echo "[*.{yaml,yml,html,js,json}]" >> .editorconfig
            echo "indent_style = space" >> .editorconfig
            echo "indent_size = 2" >> .editorconfig
            echo "" >> .editorconfig
            echo "[*.{md,nix}]" >> .editorconfig
            echo "indent_style = space" >> .editorconfig
            echo "indent_size = 2" >> .editorconfig
          fi
        '';
      in
        pkgs.mkShell {
          name = "java";
          buildInputs = with pkgs; [
            jdk
            sbt
            scalafmt
            scala-cli
            coursier
            python311
            python311Packages.numpy
            python311Packages.scipy
          ];
          shellHook = ''
            export JAVA_HOME=${jdk}
            ${generateEditorConfig}/bin/generateEditorConfig
          '';
        };
    });
}

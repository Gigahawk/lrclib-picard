{ inputs, ... }:
{
  perSystem =
    {
      pkgs,
      lib,
      config,
      ...
    }:
    {
      devShells = rec {
        venv-picard = config.devShells.venv.overrideAttrs (old: {
          buildInputs = (old.buildInputs or [ ]) ++ [ pkgs.zip ];
        });
        default = venv-picard;
      };
    };
}

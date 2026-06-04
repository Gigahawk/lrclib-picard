{ inputs, ... }:
{
  imports = [ inputs.flake-parts-python.flakeModules.default ];
  perSystem =
    {
      pkgs,
      system,
      ...
    }:
    {
      wrapPython = {
        workspaceRoot = ../.;
        pythonPackage = inputs.nixpkgs-python.packages.${system}."3.8";
        pyprojectOverridesPath = ./_pyproject-overrides.nix;
      };
    };

}

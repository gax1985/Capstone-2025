{ pkgs ? import <nixpkgs> {} }:


(pkgs.buildFHSUserEnv { 

	name = "Capstone-2025";
	targetPkgs = pkgs : (with pkgs; [

	python313
	python313Packages.pip
	python313Packages.virtualenv
	vscodium

	]);

	runScript = "bash && source .venv/bin/activate && pip install -r requirements.txt";

}).env

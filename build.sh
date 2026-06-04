#!/usr/bin/env bash

find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf

rm -rf dist
mkdir -p dist
(
  cd src || exit 1
  zip -r ../dist/lrclib_picard.zip lrclib_picard
)

#!/bin/sh
find ./instrosetta/interfaces/ -name "*.cs" -type f -delete
dotnet build
rm -r ./obj
rm -r ./bin

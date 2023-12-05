#!/bin/bash

echo -e "\nRuff Checks"
ruff check app/
echo -e "\nRuff Format"
ruff format app/ --check
echo -e "\nMyPy Checks"
mypy app/ --explicit-package-bases
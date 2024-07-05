#!/bin/bash
SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

zip -rq downloads.zip downloads

cd assignment

zip -rq data.zip uncompressed-data
rm -rf utils/__pycache__
zip -rq utils.zip utils


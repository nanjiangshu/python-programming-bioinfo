#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

OPT1="--exclude=~* --exclude=*~ --exclude=.*.sw[mopn]"

rsync -auvz -e  ssh $OPT1 --delete ./ webapp2:/data3/software/course-webapp/apps/python-programming-bioinfo/

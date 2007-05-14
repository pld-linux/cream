#!/bin/sh
export CREAM=/usr/share/vim/cream
exec gvim -U NONE -u $CREAM/creamrc "$@"

#!/bin/bash
FILENAME=$1
FILENAMEWE=$(echo $FILENAME | sed "s/.rs//" | sed "s/\/*[a-zA-Z]*\///g")

rustc $FILENAME
./"$FILENAMEWE.exe"
rm "$FILENAMEWE.exe" "$FILENAMEWE.pdb"
rustfmt $FILENAME
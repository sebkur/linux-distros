#!/bin/bash

find data -name '*.json' -exec sh -c 'jq "." --indent 2 "$1" > "$1.tmp" && mv "$1.tmp" "$1"' _ {} \;

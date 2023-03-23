#!/usr/bin/bash

i=0
for((i = 0; i < 40; i++)); do
	echo archibong >> README.md
	git add . && git commit -m "update" && git push
done

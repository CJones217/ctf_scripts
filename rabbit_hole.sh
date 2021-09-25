#!/bin/bash

file=flag

for i in {1..1001}
do
	
	if [[ $(file --mime-type -b "$file") == application/x-bzip2 ]]; then 
		mv $file flag.bz2
		file=flag.bz2
		echo $file
		#bunzip2 flag.bz2
		bunzip2 $file
		file=flag
		echo $i
	elif [[ $(file --mime-type -b "$file") == application/zip ]]; then 
		mv $file flag.zip
		file=flag.zip
		echo $file
		#unzip flag.zip
		unzip $file
		rm flag.zip
		file=flag.txt
		#file=flag.zip
		echo $i
	elif [[ $(file --mime-type -b "$file") == application/x-xz ]]; then 
		mv $file flag.xz
		file=flag.xz
		echo $file
		unxz $file
		file=flag
		echo $i
	elif [[ $(file --mime-type -b "$file") == application/gzip ]]; then
	       mv $file flag.gz
	       file=flag.gz
	       echo $file
	       gzip -d $file
	       file=flag
	       echo $i

	fi

done

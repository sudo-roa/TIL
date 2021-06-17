#!/bin/sh

ECHO='echo -e'
case `$ECHO` in
	-e)
		ECHO=echo;;
esac

print_bar()
{
	percent=$1

	column=`expr 71 \* "$percent" / 100`
	nspace=`expr 71 - "$column"`

	bar='\r['
	set dummy
	while [ $# -le "$column" ]
	do
		bar=$bar'='
		set - "$@" dummy
	done
	bar=$bar'>'

	set dummy
	while [ $# -le "$nspace" ]
	do
		bar=$bar' '
		set - "$@" dummy
	done
	bar=$bar'] '$percent'%\c'

	$ECHO "$bar"
}

i=0
while [ $i -le 100 ]
do
	print_bar "$i"
	i=`expr "$i" + 5 `
	sleep 1
done
echo

	

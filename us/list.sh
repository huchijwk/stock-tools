#!/usr/bin/env bash

TMP=$(mktemp -d)

wget ftp://ftp.nasdaqtrader.com/symboldirectory/nasdaqlisted.txt -O $TMP/nasdaq.csv
wget ftp://ftp.nasdaqtrader.com/symboldirectory/otherlisted.txt -O $TMP/other.csv

tail -n +2 $TMP/nasdaq.csv | head -n -1 | awk -F"|" '{ print $1","$2 }' >us-stock.csv
tail -n +2 $TMP/other.csv | head -n -1 | awk -F"|" '{  sub("\r", "", $NF);  print $NF","$2 }' >>us-stock.csv

rm -rf $TMP

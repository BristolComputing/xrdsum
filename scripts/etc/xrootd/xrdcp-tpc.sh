#!/bin/sh

# from https://github.com/snafus/cephsum/blob/master/scripts/xrdcp-tpc.sh
#Original code
#/usr/bin/xrdcp --server -f $1 root://$XRDXROOTD_PROXY/$2

# Get the last two variables as SRC and DST, all others are assumed as additional arguments
OTHERARGS="${@:1:$#-2}"
DSTFILE="${@:$#:1}"
SRCFILE="${@:$#-1:1}"


/usr/bin/xrdcp $OTHERARGS --server -f $SRCFILE root://$XRDXROOTD_PROXY/$DSTFILE

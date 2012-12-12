#!/bin/bash
set -e

CURRDIR=$(dirname $(readlink -f ${BASH_SOURCE[0]}))
APPROOT=`readlink -f ${CURRDIR}/..`

#check if it is the same as in etc/config.py
DBFILENAME="${APPROOT}/var/db/libapp.db"
INITDBFILE="${APPROOT}/var/db/libapp_db_init.sql"

if [  -f ${DBFILENAME} ]
then
	echo "${DBFILENAME} allready exists - remove it first then repeat your try ..."
else
	touch ${DBFILENAME}
	sqlite3 ${DBFILENAME} < ${INITDBFILE} && echo "${DBFILENAME} successfully initialized ..."
fi

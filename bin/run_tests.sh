#!/bin/bash
set -e

CURRDIR=$(dirname $(readlink -f ${BASH_SOURCE[0]}))
APPROOT=`readlink -f ${CURRDIR}/..`

export PYTHONPATH=${PYTHONPATH}:${APPROOT}/..
${APPROOT}/tryme/bin/python -m unittest discover ${APPROOT}/src/test/unit "*.py"
${APPROOT}/tryme/bin/python -m unittest discover ${APPROOT}/src/test/integration "*.py"

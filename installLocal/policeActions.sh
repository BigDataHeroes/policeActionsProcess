#!/bin/bash

source activate keepcodingFinalProject
source properties.sh

python policeActions.py $inputF $outputF

#!/bin/sh

output=$1
math=$2
jobid=$(sed -n 's/Job ID: //p' $math"/"config1.txt)

mkdir $output$jobid

wget -q "https://raw.githubusercontent.com/spatrickdoyle/physics-research/master/assets/test_image1.png"
mv test_image1.png $output$jobid/.

wget -q "https://raw.githubusercontent.com/spatrickdoyle/physics-research/master/assets/test_image2.png"
mv test_image2.png $output$jobid/.

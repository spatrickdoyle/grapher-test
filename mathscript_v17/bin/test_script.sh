#!/bin/sh

jobid=$(sed -n 's/Job ID: //p' ./config1.txt)

mkdir ../plots/Jobs/$jobid

wget -q "https://raw.githubusercontent.com/spatrickdoyle/physics-research/master/assets/test_image1.png"
mv test_image1.png ../plots/Jobs/$jobid/.

wget -q "https://raw.githubusercontent.com/spatrickdoyle/physics-research/master/assets/test_image2.png"
mv test_image2.png ../plots/Jobs/$jobid/.

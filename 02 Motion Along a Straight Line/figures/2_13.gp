set size 0.625,0.625
set terminal latex
set output "2_13.tex"
set autoscale
unset log
unset label
set xtic auto
set ytic auto
set xlabel "Time (s)"
set ylabel "Speed (mi/h)"
plot "2_13.dat" title "" with linespoints pt 7

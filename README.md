# fly-straight-dammit
The fly straight dammit sequence which when plotted, initially seems chaotic, but after six hundred thirty eight iterations, instantly stabilizes

For every choice of initial term a(0) 

there exist integers r and t >= 0 

such that a(2*r+4*t+0) = 1, 

a(2*r+4*t+1) = 2*r+4*t+3, 

a(2*r+4*t+2) = 2*(2*r+4*t+3), 

a(2*r+4*t+3) = 2. 

It is conjectured that quasi-periodic sequences exist only for R = 0, 1, 2 or 3 in a(n) = a(n-1) + n + R and that for R >= 4 the recurrence is not quasi-periodic. For R = 0, 1, 2 all starting values give a quasi-periodic sequence. The respective loop is (1, x) for R = 0, (1, x, 2x, 2) for R = 1 (this sequence), (1, x, 2x, x) or (2x, x) for R = 2. For R = 3 only some starting values converge to a 6-loop (4x+2, 2x+1, 3x+6, x+2, 2x+9, 3x+17). 
                                                                           - [Ctibor O. Zizka](https://oeis.org/wiki/User:Ctibor_O._Zizka)

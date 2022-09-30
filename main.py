import numpy as np
import matplotlib.pyplot as plot
import math
from matplotlib.animation import FuncAnimation

frs,srs,trs=[],[],[]
fr,sr,tr=0,0,0
fns,sns,tns=[],[],[]
fn,sn,tn=0,0,0
"""
f is for first, s for second and t for third
r is the radius 
n is the integer 
"""
while fn<=360 and fr<=100:
    fr = ((1 + math.sqrt(5)) / 2) ** ((2 / np.pi) * fn)
    frs.append(fr)
    fns.append(fn)
    fn+=0.1

while sn<=360 and sr<=100:
    sr = ((2 + math.sqrt(8)) / 2) ** ((2 / np.pi) * sn)
    srs.append(sr)
    sns.append(sn)
    sn+=0.1

while tn<=360 and tr<=100:
    tr = ((3 + math.sqrt(13)) / 2) ** ((2 / np.pi) * tn)
    trs.append(tr)
    tns.append(tn)
    tn+=0.1



plot.axes(projection='polar')
plot.title('Logarithimic Spirals')
plot.plot(fns,frs, 'r')
plot.plot(sns,srs, 'b')
plot.plot(tns,trs, 'g')
plot.show()
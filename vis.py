import pandas as pd
import matplotlib.pyplot as pp
import numpy as np

df=pd.read_csv('evpd.csv')
print(df)

ff=df['County'].value_counts()
pp.figure(figsize=(6,4))
ff.plot(kind='bar')
pp.xlabel('County')
pp.ylabel('Fequency')
pp.tight_layout()
# pp.show()

pp.savefig('cvfr.jpg')

text='''
<!DOCTYPE html>
<html lang="en">
<head>
   <meta charset="UTF-8">
   <link rel="stylesheet" href="style.css">
   <title>Python HTML app</title>
</head>
<body>
    <nav>
        <h1>
            Analytics Dashboard
        </h1>
    </nav>
    <div class="card">
        <h2>
            County v/s Frequency
        </h2>
        <img src="cvfr.jpg" alt="">
        <p>
            This chart shows how often different counties appear in the data. King County stands out by a huge margin, with way more entries than any other. After that, counties like Clark, Snohomish, and Kitsap show up a fair amount, but nowhere near as much as King. Most of the other counties have much smaller numbers, and some barely show up at all. This tells us that whatever this data is measuring, it is happening a lot more in King County compared to the rest. The numbers drop off quickly after the top few, which means the data is really focused in just a few places
        </p>
    </div>

'''
f=open('kh.html','w')
f.write(text)

pp.clf()

l=list(df['Vehicle Location'])
x=[float(e.split('(')[1].split(' ')[0]) for e in l]
y=[float(e.split('(')[1].split(' ')[1][0:-1]) for e in l]
pp.xlabel('X-Cood.')
pp.ylabel('Y-Cood.')
pp.scatter(x,y)
# pp.show()
pp.savefig('loc.jpg')

text='''

    
    <div class="card">
        <h2>
            Vehicle Location Scatter-Plot
        </h2>
        <img src="loc.jpg" alt="">
        <p>
            This scatter plot tells us about the area in which most of the EV vehicles were located. According to this scatter plot, we can easily point out that the most densed x-cood. range is [-127,-121]. Furthermore, the most densed y-cood. range is [47,48.5]. Hence, we can easily find out the region in which most vehicles were located.
        </p>
    </div>
'''
f.write(text)

pp.clf()

ff=df['Electric Utility'].value_counts()
ff.plot(kind='bar')
pp.xlabel('Electric Utility')
pp.ylabel('Fequency')
# pp.show()
pp.savefig('eu.jpg')
text='''

   
    <div class="card">
        <h2>
            Vehicle Location Scatter-Plot
        </h2>
        <img src="eu.jpg" alt="">
        <p>
            This chart shows how often different electric utility appear in the data. CITY OF SEATTLE - (WA)|CITY OF TACOMA - (WA) stands out by a huge margin, with way more entries than any other. After that, a few utilities show up a fair amount, but nowhere near as much as CITY OF SEATTLE - (WA)|CITY OF TACOMA - (WA). Most of the other utilities have much smaller numbers, and some barely show up at all. This tells us that whatever this data is measuring, it is happening a lot more in CITY OF SEATTLE - (WA)|CITY OF TACOMA - (WA) compared to the rest. The numbers drop off quickly after the top few, which means the data is really focused in just a few places
        </p>
    </div>
    </nav>
    </body>
    </html>
'''

f.write(text)
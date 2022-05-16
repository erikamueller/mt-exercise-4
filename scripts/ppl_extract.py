import pandas as pd
import sys

logfile= sys.argv[1]
# logfile = "postnorm.log"

resultdict={}


with open(logfile,'r',encoding='utf8') as f:
    for line in f:
        # resultdict['prenorm']=[]
        if "Validation result (greedy)" in line:
            step = int(line[99:106].strip())
            # resultdict['postnorm'].append(float(line[145:153].strip()))
            resultdict[step] = float(line[145:153].strip())

print(resultdict)            



df = pd.DataFrame(data=resultdict,index=[0])

df = (df.T)

df.to_csv(logfile+".csv")
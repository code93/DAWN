import re

with open('fishSequences.txt') as f:
    lines = f.readlines()

fishes = []
for line in lines:
    try:
        if type(int(line.strip())) == int:
            fishes.append(int(line.strip()))
    except:
        continue


print(fishes)

seq = []
sequences = []
for i in range(0,len(fishes)-1):
    if fishes[i]<fishes[i+1]:
        seq.append(fishes[i])
    if fishes[i]>fishes[i+1]:
        sequences.append(seq)
        seq = []

with open("fishList.txt", "w") as h: 
    h.write(str(sequences))


print(sequences)
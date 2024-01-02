## Code followed from online tutorial as used this to find a solution that was not so memory/cpu intensive

inputs, *blocks = open('day5/day5_input.txt').read().split("\n\n")
inputs = list(map(int, inputs.split(":")[1].split()))

#print(inputs)
seeds=[]
for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i+1]))
#print(seeds)
for block in blocks:
    #print(block)
    ranges=[]
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new=[]
    while len(seeds) > 0:
        s, e = seeds.pop()
        for a, b, c in ranges:
            os = max(s, b)
            oe = min(e, b + c)
            if os < oe:
                new.append((os - b + a, oe - b + a))
                if os > s:
                    seeds.append((s, os))
                if e > oe:
                    seeds.append((oe, e))
                break
        else:
            new.append((s,e))
    seeds=new
print(seeds)
print(min(seeds)[0])    
#print(seeds)
#print(sorted(seeds))
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
if(len(strs) < 2):
    print([strs])
result = {}
for s in strs:
    temp = ''.join(sorted(s))
    result[temp] = result.get(temp, []) + [s]
r = []
for w in result.values():
    r.append(w)
print(r)

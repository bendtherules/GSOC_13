r=open("galFiltered.nnf","r")
w=open("result2.json","w")
nodes=[]
w.write("[\n")
for p in r:
    if nodes:
        if not gave_newline:
            gave_newline=True
            w.write(",\n")
    temp=p[:-1].split(" ")[3:]
    if temp[0] not in nodes:
        nodes.append(temp[0])
        w.write('{ data: { id: "'+temp[0]+'" }, group: "nodes" }')
        gave_newline=False
    if len(temp)>1:
        if temp[2] not in nodes:
            if not gave_newline:
                w.write(",\n")
            nodes.append(temp[2])
            w.write('{ data: { id: "'+temp[2]+'" }, group: "nodes" },\n')
            gave_newline=True
    if not gave_newline:
        w.write(",\n")
    w.write('{ data: { id: "'+ temp[0]+" ("+temp[1]+") "+temp[2]+'", source: "'+temp[0]+'", target: "'+temp[2]+'" }, group: "edges" }')
    gave_newline=False

w.write("\n]")
w.close()
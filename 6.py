names=["ammu","appu","malavika","arun"]
count=0
for x in names:
    for i in x:
        if i in x:
            if i=="a":
                count+=1
                print("no.of a in the list:",count)
p=lambda j:list(map(list,zip(*[[x for x in c if x]+[0]*c.count(0)for c in zip(*j)])))

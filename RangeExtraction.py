def rangeextraction(args):
    rs = []
    t = []
    for i in range(len(args)-1):
        t.append(args[i])
        if args[i] != args[i+1] - 1:
            rs.append(f'{t[0]}-{t[-1]}') if len(t) > 2 else rs.extend(map(str,t))
            t.clear()
    i+=1
    if args[i] == args[i-1] + 1 and len(t)+1 > 2:
        rs.append(f'{t[0]}-{args[i]}')
    else:
        t.append(args[i])
        rs.extend(map(str,t))
    return ','.join(k for k in rs)
if __name__ == "__main__":
    print(rangeextraction([-81, -80, -77, -75, -73, -70, -68, -66, -64, -61, -60, -59, -57]))

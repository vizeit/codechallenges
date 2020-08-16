"""
Given a string with each character representing a task, add cooldown period '.' 
between two repeating tasks if number of other tasks between them do no meet the
cooldown period
e.g. aba, k=2 -> ab.a
     aabb, k=3 -> a..ab..b
"""
def CoolDownScheduler(tasks, k):
    d = {}
    rs = []
    for t in tasks:
        if t in d:
            if d[t] < k:
                for j in range(k-d[t]): rs.append('.')
                for m in d: 
                    if m!=t: d[m]+= k-d[t]+1
            else:
                for m in d: 
                    if m!=t: d[m]+=1 
            rs.append(t)
            del d[t]
        else:
            rs.append(t)
            for m in d: d[m]+=1
            d[t] = 0
    return ''.join(rs)

if __name__ == "__main__":
    print(coolDownscheduler('abcacaa', 3))
    print(coolDownscheduler('aba', 2))
    print(coolDownscheduler('aabb', 3))

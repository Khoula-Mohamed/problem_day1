class meeting:
    
    def __init__(self, start, end, pos):
        
        self.start = start
        self.end = end
        self.pos = pos

def maxMeeting(l, n):
 
    ans = []
    l.sort(key = lambda x: x.end)
    ans.append(l[0].pos)
    time_limit = l[0].end
    
    for i in range(1, n):
        if l[i].start > time_limit:
            ans.append(l[i].pos)
            time_limit = l[i].end

    for i in ans:
        print(i + 1, end = " ")
        
    print()

if __name__ == '__main__':
    start = [ 1, 3, 0, 5, 8, 5 ]
    end = [ 2, 4, 6, 7, 9, 9 ]
    n = len(start)
    l = []
    for i in range(n):
        
        l.append(meeting(start[i], end[i], i))
    print("The meetings that can be scheduled in one room such that number of meetings is maximum are:")     
    maxMeeting(l, n)
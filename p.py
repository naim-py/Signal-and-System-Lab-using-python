if __name__ == "__main__":
    n = int(input())
    em_list = []
    for i in range(n):
        str = input()
        l = str.split()

        if l[0]== 'insert':
            em_list.insert(int(l[1]),int(l[2]))
        elif l[0] == 'print':
            print(em_list)
        elif l[0] == 'remove':
            em_list.remove(int(l[1]))
        elif l[0] == 'append':
            em_list.append(int(l[1]))
        elif l[0] == 'sort':
            em_list.sort()
        elif l[0] == 'pop':
            em_list.pop()
        else:
            em_list.reversed()
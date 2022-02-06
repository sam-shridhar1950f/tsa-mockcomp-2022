#txt file of input
f = "input.txt"
N = 4

#initialize list of cows
cows_list = []
a_file = open(f, "r")


cows_list = [(line.strip()).split() for line in a_file]


a_file.close()

      
#
matches = 0
for i in range(N - 1):
    set_cow = set(cows_list[i])
    for j in range(N - 1):
        res = None
        next_set = set(cows_list[j])
        
        if i == j:
            continue
        else:
            if (set_cow & next_set):
                res = True
            else:
                res = False
        
        if res == True:
            matches += 1


print(matches)




    

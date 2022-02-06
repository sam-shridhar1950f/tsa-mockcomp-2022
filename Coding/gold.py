

# question params

my_file = open("sample.txt", "r")
content = my_file.read()
content_list = content.split(",")
my_file.close()
content_list = content_list[1:]

test_list = [int(item) for item in content_list]

nums = [min(test_list), max(test_list)]
num_multiples = (max(nums) // 12) + 1
multiples = []
for i in range (1,num_multiples):
  multiples.append(12*i)


cnt = 0
counted_numbers = []
for i in range(len(test_list) - 1):
  for j in range(len(multiples) - 1):
    if test_list[i] > multiples[j] and test_list[i] < multiples[j + 1] and test_list[i+1] < multiples[j + 1] and test_list[i+1] > multiples[j]:
      if test_list[i] not in counted_numbers or test_list[i + 1] not in counted_numbers:

        counted_numbers.append(test_list[i])
        counted_numbers.append(test_list[i + 1])
      
        cnt += 1
    elif test_list[i] > multiples[j] and test_list[i] < multiples[j + 1]:
      if test_list[i] not in counted_numbers:
        counted_numbers.append(test_list[i])
      
        cnt += 1
    else:
      continue

print(cnt*12)










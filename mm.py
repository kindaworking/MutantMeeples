import random

my_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R"]

random.shuffle(my_list)
// Need to work out how I want ot get my list. Will likely end up using random.sample. 
print("From the shuffle: " + my_list[0] + "," + my_list[1])

print("From the sample: " + str(random.sample(my_list,2)))

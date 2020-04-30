def mean(mylist):
    print("Function Started!!...")
    the_mean=sum(mylist)/len(mylist)
    return the_mean

my_mean=mean([1, 4, 5])
print(my_mean + 10)

print(type(mean), type(sum), type(len))
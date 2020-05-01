def mean(value):
    if type(value) == dict:
        the_mean=sum(value.values()) / len(value)
    else:
     the_mean=sum(value)/len(value)

    return the_mean

temp=[20,1,30,3,31]
student_grade={"Marie": 20.1,"John": 30.3, "Sam": 31}
print(mean(student_grade))
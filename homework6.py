my_dict = {"Marya":1992, "Mike":1983, "Sam":1981}
print(my_dict)
print(my_dict["Marya"])
print(my_dict.get("Ann"))
my_dict.update({"Anton":1985,
               "Eva":1987})
a=my_dict.pop("Eva")
print(a)
print(my_dict)


my_set = {55,66,77,88,44,99,77,88,"Faith","Love","Love"}
print(my_set)
my_set.update({"Hope", 33})
print(my_set.remove("Love"))
print(my_set)
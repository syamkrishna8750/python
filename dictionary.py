my_dict={'b':2,'a':1,'d':4,'c':3}
asc_dict=dict(sorted(my_dict.items()))
des_dict=dict(sorted(my_dict.items(),reverse=True))
print("orginal dictionary:",my_dict)
print("Ascending order:",asc_dict)
print("descending order:",des_dict)
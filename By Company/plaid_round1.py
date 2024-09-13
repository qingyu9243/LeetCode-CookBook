"""
- routing number - sequnce of digit to identity number
wells fargo has xx rounting num


- bank name (string, bank of ameria/ boa )


- bank ids (unique id for banks)


database 1
{
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
}
one - to - one relationship (id is unique)

database 2
# These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]

[
  # There are multiple common ways to write the name of this bank
  ("Wells Fargo", 1),
  ("Wells", 1),

  ("Chase", 2),
  ("Capital One", 3),
  ("Bank of America", 4),

  # These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]

many - to - many relationship 


part 1: question: 2 database as input, output is below:

key: rounting, value: list of id/single id

example output:
123 -> 1
456 -> 2
789 -> 3
555 -> 5,6


# create_routing_number_mapping combines a 1 to 1 map from routing number to bank name with a many to many relationship
# to create a single mapping between routing numbers and Bank IDs.
def create_routing_number_mapping(rn_to_name: Dict[str, str], name_to_bank_id: List[Tuple[str, int]]):
  pass
"""
from typing import Dict, List, Tuple
from collections import defaultdict
def create_routing_number_mapping(rn_to_name: Dict[str, str], name_to_bank_id: List[Tuple[str, int]]):
    dict_db2 = defaultdict(list)
    res_dict = {}

    # construct dict_db2 as flatten name_to_bank_id
    for bank_name, bank_id in name_to_bank_id:
        dict_db2[bank_name].append(bank_id)
    
    # find bank name in rn_to_name and save bank id list to result dict
    for routing_id, bank_name_rn in rn_to_name.items():
        if bank_name_rn in dict_db2:
            res_dict[routing_id] = dict_db2[bank_name_rn]

    return res_dict

db1_t1 = {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
}
db2_t1 = [
    ("Wells Fargo", 1),
    ("Wells", 1),
    ("Chase", 2),
    ("Capital One", 3),
    ("Bank of America", 4),
    ("First State Bank", 5),
    ("First State Bank", 6),
]
#print(create_routing_number_mapping(db1_t1, db2_t1))

db1_t2 = {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
}
db2_t2 = [
    ("Wells Fargo", 1),
    ("Wells", 1),
    ("Chase", 2),
    ("Chase", 3),
    ("Capital One", 3),
    ("Capital One", 5),
    ("Bank of America", 4),
    ("First State Bank", 5),
    ("First State Bank", 6),
    ("Wells Fargo", 8),
    ("Wells Fargo", 6)
]
#print(create_routing_number_mapping(db1_t2, db2_t2))

db1_t3 = {
    "123": "Wells Fargo",
    "555": "First State Bank",
}
db2_t3 = [
    ("Wells Fargo", 1),
    ("Wells", 1),
    ("Chase", 2),
    ("Chase", 3),
    ("Capital One", 3),
    ("Capital One", 5),
    ("Bank of America", 4),
    ("First State Bank", 5),
    ("First State Bank", 6),
    ("Wells Fargo", 8),
    ("Wells Fargo", 6)
]
#print(create_routing_number_mapping(db1_t3, db2_t3))

db1_t4 = {
    "123": "Wells Fargo",
    "456": "Chase",
    "789": "Capital One",
    "555": "First State Bank",
}
db2_t4 = [
    ("Wells Fargo", 1),
    ("Wells", 1),
    ("Chase", 2),
    ("Chase", 3),
]
#print(create_routing_number_mapping(db1_t4, db2_t4))

####### part 2 #######
# rounting map 
"""
database 1
{
    "123": "Wells Fargo",
    "456": ["Chase",]
    "789": "Capital One",
    "555": "First State Bank", "First state"
}
some errors in db1.

[
  {
    "123": "Wells Fargo",
    "456": "Chase",
  },
  {
    "123": "Wells",
    "789": "Capital One",
    "456": "Bank of America",
  },
  {
    "123": "Bank of America",
    "456": "Chase",
  },
]

database 2

[
  # There are multiple common ways to write the name of this bank
  ("Wells Fargo", 1),
  ("Wells", 1),

  ("Chase", 2),
  ("Capital One", 3),
  ("Bank of America", 4),

  # These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]

output:
456: [2, 4]
123: [1, 4]
789: [3]

dict_1 = ["123":["Wells Fargo", "Wells", "Bank of America"]]
dict_2 = "name": 2, 3...
res_dict = [1, 1, 4] -> 123: {1:2, 4:1} (routting -> dict of id count)
final = 
"""
def create_routing_number_mapping_2(rn_to_name: List[Dict[str, str]], name_to_bank_id: List[Tuple[str, int]]):
    # 
    dict_rount_to_bank_list = defaultdict(list)
    for dict in rn_to_name:
        for rounting, name in dict.items():
            dict_rount_to_bank_list[rounting].append(name)

    list_bank_name_ids = defaultdict(list)
    for bank_name, bank_id in name_to_bank_id:
        list_bank_name_ids[bank_name].append(bank_id)
    
    res = defaultdict(list)
    for rnt_num, bank_list in dict_rount_to_bank_list.items():
        for bank in bank_list:
            if bank in list_bank_name_ids:
                res[rnt_num].extend(list_bank_name_ids[bank])
    
    return res

p2_db1_t1 = [
  {
    "123": "Wells Fargo",
    "456": "Chase",
  },
  {
    "123": "Wells",
    "789": "Capital One",
    "456": "Bank of America",
  },
  {
    "123": "Bank of America",
    "456": "Chase",
  },
]
p2_db2_t1 = [
  # There are multiple common ways to write the name of this bank
  ("Wells Fargo", 1),
  ("Wells", 1),

  ("Chase", 2),
  ("Capital One", 3),
  ("Bank of America", 4),

  # These are two different banks with the same name
  ("First State Bank", 5),
  ("First State Bank", 6),
]
#rint(create_routing_number_mapping_2(p2_db1_t1, p2_db2_t1))



"""

"""
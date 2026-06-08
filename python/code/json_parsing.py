import json
import pprint as pp

# Method loads deserialize a string to a python object by using the below format table
# JSON        python
# object      dict
# string      str
# Array       list
# ...etc


# dns_servers = '{"dns": {"types": ["root", "tld", "authoritative"], "public_dns": "8.8.8.8"}}'
#
# print('dns_servers varibale type:', type(dns_servers))
# data = json.loads(dns_servers)
# print(data)
# print('data variable type:', type(data))


# method load deserialize a fp(file pointer) to a python object

# with open('breed.json', 'r') as f:
#     data = json.load(f)
#     pp.pprint(data)


# method dumps serialized python object data into json formatted string

# course_teach = {
#     'name': 'rahul shetty',
#     'course': ['java', 'python', 3],
#     'udemy': True,
#     'Influencer': None
# }
#
#
# json_str = json.dumps(course_teach)
# print(json_str)


# method dump
uid = {
    'uid': '394jdndk-sdfjntla9thda'
}

with open('breed.json', 'a') as f:
    json.dump(uid, f)
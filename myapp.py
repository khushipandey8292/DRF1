import requests
import json

# URL="http://127.0.0.1:8000/studentapi/"
# def get_data(id=None):
#     data={}
#     if id is not None:
#         data={'id':id}
#     json_data=json.dumps(data)
#     r=requests.get(url=URL,data=json_data)
#     data=r.json()
#     print(data)
# # get_data(1)

# def post_data():
#     data={
#         'name':'khushboo',
#         'roll':160,
#         'city':'bareilly'
#     }
#     json_data=json.dumps(data)
#     r=requests.post(url=URL,data=json_data)
#     data=r.json()
#     print(data)
# post_data()

# def update_data():
#     data={
#         'id':'1',
#         'name':'khushi',
#         'city':'patna'
#     }
#     json_data=json.dumps(data)
#     r=requests.put(url=URL,data=json_data)
#     data=r.json()
#     print(data)
# # update_data()

# def delete_data():
#     data={
#         'id':'1'
#     }
#     json_data=json.dumps(data)
#     r=requests.delete(url=URL,data=json_data)
#     data=r.json()
#     print(data)
# # delete_data()


# URL="http://127.0.0.1:8000/student_view_api/"
URL="http://127.0.0.1:8000/studentapi/"
def get_data(id=None):
    data={}
    if id is not None:
        data={'id':id}
    json_data=json.dumps(data)
    headers={'content-Type':'application/json'}
    r=requests.get(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
get_data()

def post_data():
    data={
        'name':'shivani',
        'roll':164,
        'city':'rampur'
    }
    headers={'content-Type':'application/json'}
    
    json_data=json.dumps(data)
    r=requests.post(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# post_data()

def update_data():
    data={
        'id':'1',
        'name':'sita',
        'city':'kanpur'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.put(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# update_data()

def delete_data():
    data={
        'id':'1'
    }
    headers={'content-Type':'application/json'}
    json_data=json.dumps(data)
    r=requests.delete(url=URL,headers=headers,data=json_data)
    data=r.json()
    print(data)
# delete_data()
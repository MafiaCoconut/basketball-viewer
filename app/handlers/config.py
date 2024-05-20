def get_token():
    with open('.env') as f:
        return f.read().split('\n')[0]


# def get_admin_id():
#     with open('.env') as f:
#         return f.read().split('\n')[1]
#

def get_type_of_device():
    with open('../.env') as f:
        return f.read().split('\n')[1]



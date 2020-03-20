import sys
import requests
import json
from pandas import json_normalize

def main():

    if len(sys.argv) < 4:
        usage()
    else:
        url = build_url(sys.argv)
        if len(url) == 0:
            usage()
        else:
            resp = requests.get(url)

            if resp.status_code != 200:
                print(url + ' returned status code ' + str(resp.status_code))
                print_json(resp.json())
            else:
                data = json.loads(json.dumps(resp.json()))
                toCSV(sys.argv[1], data)
                print('MPAC ran successfully')

def build_url(args):
    url, path = '', ''
    if args[1] == 'member':
        path = '/get-user?email={}&key={}'.format(args[2], args[3])
    elif args[1] == 'ticks':
        path = '/get-ticks?email={}&key={}'.format(args[2], args[3])
    elif args[1] == 'todos':
        path = '/get-to-dos?email={}&key={}'.format(args[2], args[3])
    elif args[1] == 'routes':
        if lat_lon(args):
            path = '/get-routes-for-lat-lon?lat={}&lon={}&key={}'.format(args[2], args[3], args[4])
        else:
            routeIds = build_id_str(args)
            memberKey = get_member_key(args)
            if len(routeIds) > 0 and len(memberKey) > 0:
                path = '/get-routes?routeIds={}&key={}'.format(routeIds, memberKey)

    if len(path):
        url = 'https://www.mountainproject.com/data' + path
    return url

def lat_lon(args):
    return ('.' in args[2] or '.' in args[3]) and (len(args) == 5)

def build_id_str(args):
    ids = ''
    args = args[2:-1]
    for arg in args:
        ids += arg + ','
    return ids.rstrip(',')

def get_member_key(args):
    key = args[-1:]
    return key[0]

def toCSV(method, input):
    if method == 'member':
        json_normalize(input).to_csv('mp-member.csv', index=False)
    elif method == 'ticks':
        json_normalize(input, 'ticks', ['hardest','average']).to_csv('mp-member-ticks.csv', index=False)
    elif method == 'todos':
        json_normalize(input, 'toDos', record_prefix='To-Do').to_csv('mp-member-todos.csv', index=False)
    elif method == 'routes':
        json_normalize(input, 'routes').to_csv('mp-routes.csv', index=False)

def print_json(input):
    for item in input.items():
        if isinstance(item[1], dict):
            print('{}: '.format(item[0]))
            print_json(item[1])
        elif isinstance(item[1], list):
            for item in item[1]:
                if isinstance(item, dict):
                    print_json(item)
        else:
            print('{}: {}'.format(item[0], item[1]))

def usage():
    print('''
Use this program to retrieve member- or route-specific information from mountainproject.com.
Results are stored in one of four .csv files, depending on the value of the first parameter; i.e.\n
  Parameter   Filename
  ---------   -------------------
  member      mp-member.csv
  ticks       mp-member-ticks.csv
  todos       mp-member-todos.csv
  routes      mp-routes.csv\n
USAGE: (for member-specific information)\n
  $ python mp_dump.py member|ticks|todos member@domain.com member-key\n
  where member|ticks|todos is the type of information you want (specify only one at a time),
  member@domain.com is the email address to which the desired mountainproject member is registered, and
  member-key is the mountainproject-assigned private key associated with the member\'s email address (see API docs).\n
EXAMPLE:\n
  $ python mp_dump.py member me@gmail.com 13258-2f62370fe45c3896e8d1500f4777bd68\n
  The above command retrieves information about the member registered to me@gmail.com.\n
USAGE: (for route-specific information)\n
  $ python mp_dump.py routes routeId1 [routeId2...] member-key\n
  where routeId1 [routeId2...] is a list of one or more route IDs for which to retrieve information, and
  member-key is a valid mountainproject-assigned private key (see API docs).\n
EXAMPLE: (route list)\n
  $ python mp_dump.py routes 105835842 105742085 13258-2f62370fe45c3896e8d1500f4777bd68\n
  The above command retrieves information specific to route IDs 105835842 and 105742085.\n
  For information about all routes within a 30-mile radius of a geographic location, use the following convention:\n
  $ python mp_dump.py routes lat lon member-key\n
  where lat is the geographic latitude,
  lon is the geographic longitude, and
  member-key is a valid mountainproject-assigned private key (see API docs).\n
EXAMPLE: (lat-lon)\n
  $ python mp_dump.py routes 40.03 -105.25 13258-2f62370fe45c3896e8d1500f4777bd68\n
  The above command retrieves information about routes within a 30-mile radius of the specified lat-lon.
''')

if __name__ == '__main__':
    main()

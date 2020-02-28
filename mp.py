import sys
import requests
import json
import csv
from pandas import json_normalize

def main():

    if len(sys.argv) < 4:
        usage()
    else:
        url = buildURL(sys.argv)
        if len(url) == 0:
            usage()
        else:
            resp = requests.get(url)
        
            if resp.status_code != 200:
                print('{}'.format(url) + ' returned status code ' + str(resp.status_code))
                printJSON(resp.json())
            else:
                data = json.loads(json.dumps(resp.json()))
                toCSV(sys.argv[1], data)

def buildURL(args):
    url = 'https://www.mountainproject.com/data'
    if memberInfo(args[1]):
        url += buildMemberURL(args)
    elif routeInfo(args[1]):
        url += buildRoutesURL(args)
    else:
        url = ''
    return url

def memberInfo(arg):
    return arg == 'member' or arg == 'ticks' or arg == 'todos'

def routeInfo(arg):
    return arg == 'routes'

def buildMemberURL(args):
    path = ''
    if args[1] == 'member':
        path = '/get-user?email={}&key={}'.format(args[2], args[3])
    elif args[1] == 'ticks':
        path = '/get-ticks?email={}&key={}'.format(args[2], args[3])
    elif args[1] == 'todos':
        path = '/get-to-dos?email={}&key={}'.format(args[2], args[3])
    return path

def buildRoutesURL(args):
    path = ''
    if '.' in args[2] or '.' in args[3]:
        path += '/get-routes-for-lat-lon?lat={}&lon={}&key={}'.format(args[2], args[3], args[4])
    else:
        ids, key = '', ''
        rest = args[2:]
        for arg in rest:
            if '-' in arg:
                key = arg
                ids = ids[:-1]
            else:
                ids += arg + ','
        path = '/get-routes?routeIds={}&key={}'.format(ids, key)
    return path

def toCSV(method, input):
    if method == 'member':
        json_normalize(input).to_csv('mp-member.csv', index=False)
    elif method == 'ticks':
        json_normalize(input, 'ticks', ['hardest','average']).to_csv('mp-member-ticks.csv', index=False)
    elif method == 'todos':
        json_normalize(input, 'toDos', record_prefix='To-Do').to_csv('mp-member-todos.csv', index=False)
    elif method == 'routes':
        json_normalize(input, 'routes').to_csv('mp-routes.csv', index=False)

def printJSON(input):
    for item in input.items():
        if isinstance(item[1], dict):
            print('{}: '.format(item[0]))
            printJSON(item[1])
        elif isinstance(item[1], list):
            for item in item[1]:
                if isinstance(item, dict):
                    printJSON(item)
        else:
            print('{}: {}'.format(item[0], item[1]))

def usage():
    print('Use this program to retrieve member- or route-specific information from mountainproject.com.')
    print('Results are stored one of four .csv files, depending on the value of the second parameter; i.e.\n')
    print('  "member" -> mp-member.csv')
    print('  "ticks"  -> mp-member-ticks.csv')
    print('  "todos"  -> mp-member-todos.csv')
    print('  "routes" -> mp-routes.csv\n')
    print('USAGE (for member-specific information):')
    print('  For information about a mountainproject.com member, use the following convention:\n')
    print('  > python mp.py member|ticks|todos member@domain.com member-key\n')
    print('  where "member|ticks|todos" is the type of information you want (specify only one at a time).')
    print('        "member@domain.com" is the email address under which your mountainproject member is registered,')
    print('    and "member-key" is your mountainproject-assigned private key (see API docs).\n')
    print('  EXAMPLE:')
    print('    > python mp.py member me@gmail.com 13258-2f62370fe45c3896e8d1500f4777bd68\n')
    print('    The above command retrieves information about the member registered to me@gmail.com.\n')
    print('USAGE (for route-specific information):')
    print('  For information about a specific route(s), use the following convention:\n')
    print('  > python mp.py routes routeId1 [routeId2...] member-key\n')
    print('  where "routeId1 [routeId2...]" is a list of one or more route IDs for which to retrieve information,')
    print('    and "member-key" is your mountainproject-assigned private key (see API docs).\n')
    print('  EXAMPLE:')
    print('    > python mp.py routes 105835842 105742085 13258-2f62370fe45c3896e8d1500f4777bd68\n')
    print('    The above command retrieves information specific to route IDs 105835842 and 105742085.\n')
    print('  For information about all routes within a 30-mile radius of a geographic location, use the following convention:\n')
    print('  > python mp.py routes lat lon member-key\n')
    print('  where "lat" is the geographic latitude,')
    print('        "lon" is the geographic longitude,')
    print('    and "member-key" is your mountainproject-assigned private key (see API docs).\n')
    print('  EXAMPLE:')
    print('    > python mp.py routes 40.03 -105.25 13258-2f62370fe45c3896e8d1500f4777bd68\n')
    print('    The above command retrieves information about routes within a 30-mile radius of the specified lat/lon.')

if __name__ == '__main__':
    main()

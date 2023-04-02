# Veronika Musijaka 221RDB124 13.gr
import sys

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(sys.stdin.readLine().split()) for i in range(n)]

def write_responses(result):
    sys.stdout.write('\n'.join(result) + '\n')

def process_queries(queries):
    result = []
    # Use a dictionary to store contacts, with phone numbers as keys
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[cur_query.number] = cur_query.name
        elif cur_query.type == 'del':
            if cur_query.number in contacts:
                del contacts[cur_query.number]
        else:
            response = contacts.get(cur_query.number, 'not found')
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))


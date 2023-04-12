#!/usr/bin/env python3


from pymongo import MongoClient

'''Python script that provides some stats about Nginx
logs stored in MongoDB'''


def get_stats(collection, obj):
    '''Returns the number of documents in a collection'''
    return collection.count_documents(obj)


def print_stats():
    '''Prints stats'''

    con = MongoClient('mongodb://localhost:27017')
    db = con.logs
    collection = db.nginx

    print(f'{collection.estimated_document_count()} logs')

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('Methods:')

    for req in methods:
        print('\tmethods {}: {}'.format(req,
              get_stats(collection, {'method': req})))

    print('{} status check'.format(get_stats(collection,
          {'method': 'GET', 'path': '/status'})))


if __name__ == '__main__':
    print_stats()

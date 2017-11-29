#!/usr/bin/python3.6

import sqlite3

class Duck:
    #constructor
    def __init__(self, color = "white"):
        self._color = color

    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def set_color(self,color):
        self._color = color

    def get_color(self):
        return self._color


def setupDB():
    db = sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text, i1 int)')
    db.execute('insert into test(t1,i1) values (?, ?)', ('one', 1))
    db.execute('insert into test(t1,i1) values (?, ?)', ('two', 2))
    db.commit()
    #execute returns cursor(iterator)
    #cursor = db.execute('select * from test order by t1')
    cursor = db.execute('select i1, t1 from test order by i1')
    for row in cursor:
        print(row)

def main():
    donald = Duck('blue')
    donald.quack()
    donald.walk()
    print('Color:', donald.get_color())
    #returns filehandle object(iterable), read mode default, r,w,a(ppend),r+
    fh = open('lines.txt','r')
    outfile = open('out.txt','w')
    for line in fh.readlines():
        print(line,file = outfile, end = '')
    setupDB()
    print('Done.')

if __name__ == "__main__": main()
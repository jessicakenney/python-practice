#!/usr/bin/python3.6

import sqlite3

class Duck:
    #constructor
    def __init__(self, **kwargs):
        #self._color = kwargs.get('color','white') #default white
        self.variables = kwargs

    def quack(self):
        print('Quaaack!')
        return 'Quaaack!'

    def walk(self):
        print ('Walks like a duck.')

    #def set_color(self,color):
    #    self.variables['color'] = color

    #def get_color(self):
    #    return self.variables.get('color',None)

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)


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
    donald = Duck(color = 'blue')
    donald.quack()
    donald.walk()
    donald.set_variable('nose','bill')

    #print('Color:', donald.get_color())
    print('Color:', donald.get_variable('color'))
    print('Nose:', donald.get_variable('nose'))

    #returns filehandle object(iterable), read mode default, r,w,a(ppend),r+
    fh = open('lines.txt','r')
    outfile = open('out.txt','w')
    for line in fh.readlines():
        print(line,file = outfile, end = '')
    setupDB()

    import random
    print('Random: ', random.randint(1,1000))
    x = list(range(25))
    print(x)
    random.shuffle(x)
    print(x)

    import datetime
    now = datetime.datetime.now()
    print(now.year, now.month, now.day)


    print('Done.')

if __name__ == "__main__": main()
"""
@version: latest
@author: sonny
@license: Apache Licence 
@contact: 715676363@qq.com
@site: 
@software: PyCharm Community Edition
@file: test01.py
@time: 2017/4/27 21:42


"""
import pandas as pd

unames = ['user_id','gender','age','occupation','zip']

users = pd.read_table('users.dat',sep='::',header=None,names=unames)


rnames = ['user_id','movie_id','rating','timestamp']

ratings = pd.read_table('ratings.dat',sep='::',header=None,names=rnames)

print(users)

mnames = ['movie_id','title','genres']

movies = pd.read_table('movies.dat',sep='::',header=None,names=mnames)


data = pd.merge(pd.merge(ratings,users),movies)

# print (data.pivot_table('rating',rows='title',cols='gender',aggfunc='mean'))

# print data.groupby('title').size()
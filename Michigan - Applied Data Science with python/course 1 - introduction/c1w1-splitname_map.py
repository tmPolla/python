# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 11:23:55 2017

@author: Polla
Michigan - Applied DS Course 1 week 1
"""

people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name0(person):
    return person.split()[0] + ' ' + person.split()[-1]

for person in people:
    print(split_title_and_name0(person))


def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 20:30:53 2018

@author: Tirtha
"""
"""
Recursive program to generate the sequence of moves to solve Tower of Hanoi problem for any number of disks
"""
def HanoiTower(n,source,dest,storage):
    if n==1:
        print("Move disk from {source} to {dest}")
    elif n==2:
        print(f"Move a disk from {source} to {storage}")
        print(f"Move a disk from {source} to {dest}")
        print(f"Move a disk from {storage} to {dest}")
    else:
        HanoiTower(n-1,source,storage,dest)
        print(f"Move disk from {source} to {dest}")
        HanoiTower(n-1,storage,dest,source)
        
        


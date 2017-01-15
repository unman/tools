#!/usr/bin/python
"""
Created on Sun Jan 15 23:02:34 2017

Show network tree

@author: unman
"""

from qubes.qubes import QubesVmCollection
qvm_collection = QubesVmCollection()
qvm_collection.lock_db_for_reading()
qvm_collection.load()
qvm_collection.unlock_db()
qvm_collection.pop(0)

def tree(netvm, padding):
    padding = padding + '   |-> '
    for vm in netvm.connected_vms:
        if qvm_collection[vm].is_template():
            print padding,qvm_collection[vm].name,'(Tpl)'
        else:
            print padding,qvm_collection[vm].name
        if qvm_collection[vm].is_netvm() :
            tree(qvm_collection[vm], padding)         
          
padding=''
for vm in qvm_collection:
    if qvm_collection[vm].is_netvm() and not qvm_collection[vm].netvm :
        print qvm_collection[vm].name
        tree(qvm_collection[vm], padding)

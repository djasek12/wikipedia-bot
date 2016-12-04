#!/usr/bin/python

import similarity 
import wikipedia as wiki

if __name__ == '__main__':
	list1 = ['Alex', 'Billy', 'Grant', 'Allen']
	list2 = ['Alex', 'Eric', 'Danny']
	print similarity.getJaccard(list1, list2)


#!/usr/bin/python
# -*- coding: utf-8 -*- 

from source.codeGen import *

def main():
    source = "test3.m"
    #source = "test3.m"
    gen = CodeGen(source)
    gen.generate()
if __name__ == "__main__":
    main()

# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers:
    '''
    The Complex Number Class
    
    Attributes:
    real: real part of complex number
    imag: imaginary part of complex number
    '''
    
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def __repr__(self):
        if self.real == 0.0 and self.imag == 0.0:
            return "0.00"
        if self.real == 0:
            return "%.2fi" % self.imag
        if self.imag == 0:
            return "%.2f" % self.real
        return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-", abs(self.imag))
    
    def __add__(self,other):
        '''
        '+' operator overloading
        complex number addition
        
        params:
        other:- other complex number for addition
        
        return:
        result of addition 
        '''
        a=self.real+other.real
        b=self.imag+other.imag
        return complex_numbers(a,b)
    
    def __sub__(self,other):
        '''
        '-' operator overloading
        complex number subtraction
        
        params:
        other:- other complex number for subtraction
        
        return: 
        result of subtraction 
        '''
        a=self.real-other.real
        b=self.imag-other.imag
        return complex_numbers(a,b)
    
    def __mul__(self,other):
        '''
        '*' operator overloading
        complex number multiplication
        
        params:
        other:- other complex number for multiplication
        
        return: 
        result of multiplication 
        '''
        a=self.real*other.real - self.imag*other.imag
        b=self.real*other.imag + self.imag*other.real
        return complex_numbers(a,b)
    
    def __truediv__(self,other):
        '''
        '/' operator overloading
        complex number division
        
        params:
        other:- other complex number for division
        
        return: 
        result of division 
        '''
        a=(self.real*other.real+self.imag*other.imag)/(other.real*other.real+other.imag*other.imag)
        b=(self.imag*other.real-self.real*other.imag)/(other.real*other.real+other.imag*other.imag)
        return complex_numbers(a,b)
    
    def absolute(self):
        '''
        Absolute value of Complex number
        
        return:
        absolute value
        '''
        return np.sqrt((self.real**2)+(self.imag**2))
    
    def argument(self):
        '''
        argument value of Complex number
        
        return:
        argument value
        '''
        return math.degrees(math.atan(self.imag/self.real))
    
    def conjugate(self):
        '''
        conjugate value of Complex number
        
        return:
        conjugate value
        '''
        a,b=self.real,self.imag*-1
        return complex_numbers(a,b)


comp_1=complex_numbers(3,5)
print(comp_1)
comp_2=complex_numbers(4,4)
print(comp_2)
comp_sum=comp_1+comp_2
print(comp_sum)
comp_diff=comp_1-comp_2
print(comp_diff)
comp_prod=comp_1*comp_2
print(comp_prod)
comp_quot=comp_1/comp_2
print(comp_quot)
comp_abs=comp_1.absolute()
print(comp_abs)
comp_conj=comp_1.conjugate()
print(comp_conj)
comp_arg=comp_1.argument()
print(comp_arg)



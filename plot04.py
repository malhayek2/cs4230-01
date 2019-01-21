#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def get_x_data( ):
    x_data = np.arange( 0.0, 5.0, 0.2 )
    return x_data

def get_y_data1( x_data ):
    y_data = x_data
    return y_data 

def get_y_data2( x_data ):
    y_data = x_data * x_data
    return y_data 

def get_y_data3( x_data ):
    y_data = 4.1 * x_data
    return y_data 

def display_data( x_data, y_data1, y_data2, y_data3 ):
    plt.plot( x_data, y_data1, 'rs', x_data, y_data2, 'g--', x_data, y_data3, 'b^' )
    #plt.axis( [ -1, 6, 0, 30 ] )
    plt.ylabel( 'my data' )
    plt.show( )
    return

def main( ):
    x_data = get_x_data( )
    y_data1 = get_y_data1( x_data )
    y_data2 = get_y_data2( x_data )
    y_data3 = get_y_data3( x_data )
    display_data( x_data, y_data1, y_data2, y_data3 )
    
    return

if __name__ == "__main__":
    main( )
    

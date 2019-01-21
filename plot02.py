#!/usr/bin/env python3

import matplotlib.pyplot as plt

def get_data( ):
    x_data = [ 0, 2, 3, 4, 6 ]
    y_data = [ 1, 2, 4, 7, 13 ]
    data = [ x_data, y_data ]
    return data

def display_data( data ):
    plt.plot( data[0], data[1] )
    plt.ylabel( 'my data' )
    plt.show( )
    return

def main( ):
    data = get_data( )
    display_data( data )
    
    return

if __name__ == "__main__":
    main( )
    

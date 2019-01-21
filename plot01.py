#!/usr/bin/env python3

import matplotlib.pyplot as plt

def get_data( ):
    data = [ 1, 2, 4, 7, 13 ]
    return data

def display_data( data ):
    plt.plot( data )
    plt.ylabel( 'my data' )
    plt.show( )
    return

def main( ):
    data = get_data( )
    display_data( data )
    
    return

if __name__ == "__main__":
    main( )
    

#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def get_data( ):
    data = { 'a' : np.arange( 50 ),
             # 0, 1, 2, ..., 49
             'c' : np.random.randint( 0, 50, 50 ),
             # 50 random integers in range 0 - 49
             'd' : np.random.randn( 50 ) }
             # 50 random floats in Gaussian distribution centered at 0 and variance of 1.
    data[ 'b' ] = data[ 'a' ] + 10 * np.random.randn( 50 )
    # 'a' values plus random amount in Gaussian centered at 0 and variance of 10.
    data[ 'd' ] = np.abs( data[ 'd' ] ) * 100
    # absolute of 'd' values multiplied by 100
    return data

def display_data( data ):
    # use 'a' as the index in data to get x values
    # use 'b' as the index in data to get y values
    # use 'c' as the index in data to get color of points
    # use 'd' as the index in data to get size of points
    plt.scatter( 'a', 'b', c='c', s='d', data=data )
    plt.xlabel( 'A data' )
    plt.ylabel( 'B data' )
    plt.show( )
    return

def main( ):
    data = get_data( )
    display_data( data )
    
    return

if __name__ == "__main__":
    main( )
    

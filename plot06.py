#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

def get_data( ):
    names = [ 'fred', 'barney', 'wilma' ]
    values = [ 5.6, 1.2, 9.2 ]
    data = ( names, values )
    return data

def display_data( data ):
    names, values = data
    # make a figure that is 9 inches by 3 inches
    plt.figure( 1, figsize=(9,3) )

    # subplot in 1x3 grid, position 1
    plt.subplot( 1, 3, 1 )
    # bar graph
    plt.bar( names, values )

    # subplot in 1x3 grid, position 2
    plt.subplot( 1, 3, 2 )
    # scatter plot
    plt.scatter( names, values )

    # subplot in 1x3 grid, position 3
    plt.subplot( 133 )
    # line plot
    plt.plot( names, values )
    
    # super-title
    plt.suptitle( "Categorical Plotting" )

    plt.show( )
    return

def main( ):

    data = get_data( )
    print(data)
    display_data( data )
    
    return

if __name__ == "__main__":
    main( )
    

import numpy as np
import pandas as pd

def main( ):
    df = pd.read_csv( 'a.csv' )
    df = df[ ( df.x1 < 20 ) & ( df.x1 > 7 ) ]
    df = df[ ( df.x2 < 20 ) & ( df.x2 > 7 ) ]
    df = df[ ( df.x3 < 30 ) & ( df.x3 >= 7 )]
    df = df[ ( df.x4 < 500 ) ]
    df = df[ ( df.x6 < 300 ) ]
    df = df[ ( df.labels < 7000 ) ]
    df = df[ ( df.labels > -6500 ) ]
    
    df.to_csv( 'a-cut.csv' )

    #print( df )

    return

if __name__ == "__main__":
    main( )
    

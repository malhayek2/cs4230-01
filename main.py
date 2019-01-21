#!/usr/bin/env python3

import numpy as np
import pandas as pd
import sklearn.model_selection
import sklearn.preprocessing

def get_data( filename ):
    data = pd.read_csv( filename, index_col=0 )
    return data

def split_data( data, ratio ):
    data_train, data_test = sklearn.model_selection.train_test_split( data, test_size=ratio )
    data_train.to_csv( "data-train.csv" )
    data_test.to_csv( "data-test.csv" )
    return

def separate_predictors_and_labels( data ):
    predictors_X = data.drop( "labels", axis=1 )
    labels_Y = data[ "labels" ].copy( )
    return predictors_X, labels_Y

def scale_predictors( X ):
    scaler = sklearn.preprocessing.StandardScaler( )
    scaler.fit( X )
    X = scaler.transform( X )
    return X, scaler

def main( ):
    # np.random.seed( 42 )
    if False:
        data = get_data( "data-cut.csv" )
        #print( data )
        split_data( data, 0.20 )
    else:
        data_train = get_data( "data-train.csv" )
        train_X_raw, train_Y = separate_predictors_and_labels( data_train )
        train_X = scale_predictors( train_X_raw )
        print( train_X_raw )
        print( train_X )

    return

if __name__ == "__main__":
    main( )

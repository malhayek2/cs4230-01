import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#open data file
def get_data( filename ):
    data = pd.read_csv( filename, index_col=0 )
    return data

#display data 
def display_data( data ):
	#setting figure 1 
	plt.figure( 1, figsize=(9,6) )
	# subplot in 3x3 grid, position 1
	plt.subplot(4, 4, 1 )
	plt.scatter( data.x1,data.labels)
	plt.title('x1 Scatter')
    # subplot in 3x3 grid, position 2
	plt.subplot( 4, 4, 2 )
	plt.bar( data.x1,data.labels)
	plt.title('x1 Bar')
	
	plt.subplot( 4, 4, 3 )
	plt.scatter( data.x2,data.labels)
	plt.title('x2 Scatter')
	plt.subplot( 4, 4, 4 )
	plt.bar( data.x2,data.labels)
	plt.title('x2 Bar')

	plt.subplot( 445 )
	plt.scatter(data.x3, data.labels)
	plt.title('x3 Scatter')
	plt.subplot( 446 )
	plt.bar(data.x3, data.labels)
	plt.title('x3 Bar')

	plt.subplot( 447 )
	plt.scatter( data.x4,data.labels)
	plt.title('x4 Scatter')
	plt.subplot( 448 )
	plt.bar( data.x4,data.labels)
	plt.title('x4 Bar')

	plt.subplot( 449 )
	plt.scatter( data.x5,data.labels)
	plt.title('x5 Scatter')
	plt.subplot( 4,4,10 )
	plt.bar(data.x5, data.labels )
	plt.title('x5 Bar')


	plt.subplot( 4,4,11 )
	plt.scatter( data.x6,data.labels)
	plt.title('x6 Scatter')
	plt.subplot( 4,4,12 )
	plt.bar( data.x6,data.labels)
	plt.title('x6 Bar')

	plt.subplot( 4,4,13 )
	plt.scatter(data.x7,data.labels)
	plt.title('x7 Scatter')
	plt.subplot( 4,4,14 )
	plt.bar(data.x7,data.labels)
	plt.title('x7 Bar')
	plt.suptitle( "Plotting" )

	#plot adjustment (padding) (top, bot window space, hspace and w spance padding between graphs)
	plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.79,
                    wspace=0.35)
	plt.show( )




def main( ):
	print("here")
	data = get_data("mo.csv")
	data = data[(data.x1 < 225 )&(data.x1 >= 40)]
	data = data[(data.x2 < 50 )&(data.x2 >= 30)]
	data = data[(data.x3 < 150 )&(data.x3 >= -100)]
	data = data[(data.x4 < 130 )&(data.x4 >= 40)]
	data = data[(data.x5 >= 1)]
	data = data[(data.x6 < 100 )]
	#x7 looks somewhat clean at this point 
	data = data[ ( data.labels > -2000 ) ]

	#save new clean data
	data.to_csv( 'cut_mo.csv' )
	# newdata = get_data("cut_mo.csv")
	display_data(data)
	#print(data.labels)


if __name__ == "__main__":
    main( )

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
	plt.scatter(data.labels, data.x1)
	plt.title('x1 Scatter')
    # subplot in 3x3 grid, position 2
	plt.subplot( 4, 4, 2 )
	plt.bar(data.labels, data.x1)
	plt.title('x1 Bar')
	
	plt.subplot( 4, 4, 3 )
	plt.scatter(data.labels, data.x2)
	plt.title('x2 Scatter')
	plt.subplot( 4, 4, 4 )
	plt.bar(data.labels, data.x2)
	plt.title('x2 Bar')

	plt.subplot( 445 )
	plt.scatter( data.labels,data.x3)
	plt.title('x3 Scatter')
	plt.subplot( 446 )
	plt.bar( data.labels,data.x3)
	plt.title('x3 Bar')

	plt.subplot( 447 )
	plt.scatter( data.labels,data.x4)
	plt.title('x4 Scatter')
	plt.subplot( 448 )
	plt.bar( data.labels,data.x4)
	plt.title('x4 Bar')

	plt.subplot( 449 )
	plt.scatter( data.labels, data.x5)
	plt.title('x5 Scatter')
	plt.subplot( 4,4,10 )
	plt.bar( data.labels, data.x5)
	plt.title('x5 Bar')


	plt.subplot( 4,4,11 )
	plt.scatter( data.labels,data.x6)
	plt.title('x6 Scatter')
	plt.subplot( 4,4,12 )
	plt.bar( data.labels,data.x6)
	plt.title('x6 Bar')

	plt.subplot( 4,4,13 )
	plt.scatter(data.labels,data.x7)
	plt.title('x7 Scatter')
	plt.subplot( 4,4,14 )
	plt.bar(data.labels,data.x7)
	plt.title('x7 Bar')
	plt.suptitle( "Plotting" )

	#plot adjustment (padding) (top, bot window space, hspace and w spance padding between graphs)
	plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.79,
                    wspace=0.35)
	plt.show( )




def main( ):
	print("here")
	data = get_data("mo.csv")
	display_data(data)
	#print(data.labels)


if __name__ == "__main__":
    main( )

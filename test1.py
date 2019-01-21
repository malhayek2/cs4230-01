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
	plt.figure( 1, figsize=(9,5) )
	# subplot in 3x3 grid, position 1
	plt.subplot(3, 3, 1 )
	plt.plot(data.x1,data.labels)
	plt.title('x1')
    # subplot in 3x3 grid, position 2
	plt.subplot( 3, 3, 2 )
	plt.plot(data.x2,data.labels)
	plt.title('x2')
	plt.subplot( 333 )
	plt.plot(data.x3, data.labels)
	plt.title('x3')
	plt.subplot( 334 )
	plt.plot(data.x4, data.labels)
	plt.title('x4')
	plt.subplot( 335 )
	plt.plot(data.x5, data.labels)
	plt.title('x5')
	plt.subplot( 336 )
	plt.plot(data.x6, data.labels)
	plt.title('x6')
	plt.subplot( 337 )
	plt.plot(data.x7, data.labels)
	plt.title('x7')
	plt.suptitle( "Plotting" )

	#plot adjustment (padding) (top, bot window space, hspace and w spance padding between graphs)
	plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.49,
                    wspace=0.35)
	plt.show( )




def main( ):
	print("here")
	data = get_data("mo.csv")
	display_data(data)
	#print(data.labels)


if __name__ == "__main__":
    main( )

from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();


if (rank == 0):
	data11 = 1.5
	#mpi.send(data1, dest = 1, tag = 100)
	mpi.send(data11, dest = 1)

	data12 = 0.5
	#mpi.send(data2, dest = 1, tag = 200)
	mpi.send(data12, dest = 1)


if (rank == 1):
	#data1 = mpi.recv(source = 0, tag = 100)
	#data2 = mpi.recv(source = 0, tag = 200)
	data01 = mpi.recv(source = 0)
	data02 = mpi.recv(source = 0)	
	print(data01, data02)

	


	
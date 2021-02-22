from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();
if (rank == 0):
	data_0_to_1 = 5.0
	mpi.send(data_0_to_1, dest = 1)
	print("sending from 0 to 1", data_0_to_1)

if (rank == 1):
	data = mpi.recv(source = 0)
	print("receiving from 0", data)


	
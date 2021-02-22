from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();


if (rank == 0):
	data_0_to_1 = 1.5
	req = mpi.isend(data_0_to_1, dest = 1)
	data_0_to_1 = 1.0
	req.wait()


if (rank == 1):
	req = mpi.irecv(source = 0)
	data = req.wait()
	print("proc 1 receiving from 0", data)
	


	
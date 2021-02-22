from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();

randNum = np.random.random_sample(2)
#randNum = np.random.rand()

if (rank == 0):
	data_0_to_1 = 1.5
	data_recd = mpi.sendrecv(data_0_to_1, dest = 1, source = 1)
	print("receiving 0 from 1", data_recd)


if (rank == 1):
	data_1_to_0 = 4.3
	data_recd = mpi.sendrecv(data_1_to_0, dest = 0, source = 0)
	print("receiving 1 from 0", data_recd)
	


	
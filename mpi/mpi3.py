from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();

randNum = np.random.random_sample(2)
#randNum = np.random.rand()

if (rank == 0):
	randNum = np.random.random_sample(2)
	#randNum = np.random.rand()
	print("Process", rank, "creates a random no and sends to 1", randNum)
	mpi.Send(randNum, dest = 1)

if (rank == 1):
	print("Process", rank, "init no", randNum)
	mpi.Recv(randNum, source = 0)
	print("Process", rank, "receives no from 0", randNum)
	


	
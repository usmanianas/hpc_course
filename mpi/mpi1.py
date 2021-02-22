from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();
if (rank == 0):
	print("no of procs:", nprocs)

print("Hi from process", rank)	
from datetime import datetime
from mpi4py import MPI
import numpy as np

mpi = MPI.COMM_WORLD
rank = mpi.Get_rank()
nprocs = mpi.Get_size();

'''
if (rank == 0):
	send_data = 20
else:
	send_data = "Nothing"	

recv_data = mpi.bcast(send_data, root = 0)

print("rank=", rank, "recv_data=", recv_data)

if (rank == 0):
	send_data = [10, 20, 30, 40]
else:
	send_data = "Nothing"	

recv_data = mpi.scatter(send_data, root = 0)

print("rank=", rank, "recv_data=", recv_data)
	
'''

data = rank**2

recv_data = mpi.gather(data, root = 3)

if rank == 3:
	print(recv_data)
	
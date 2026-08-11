from Mera_Matrix import Matrix
matrix=Matrix(2,2)
matrix.data=[[1,2],[3,4]]
result=matrix.transpose()
assert result.data==[[1,3],[2,4]]
print("Transpose test passed")

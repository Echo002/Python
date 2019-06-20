import numpy as np
from sklearn.decomposition import PCA
# a = np.array([[0.02, -0.2],[-0.2, 8]])
# b = np.linalg.eig(a)
# print(b[0])
# print(b[1])

# a = np.array([[0, -2], [0.1, 0], [-0.1, 2]])
# b = np.array([[-0.025], [-1]])
# c = a @ b
# print(c)

X = np.array([[1, 1], [1.1, 3], [0.9, 5]])
pca = PCA(n_components=1)
pca.fit(X)
print(pca.transform(X))






	
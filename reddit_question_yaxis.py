import json
import numpy as np
import matplotlib.pyplot as plt

with open("vector_field.json") as f:
    vector_field = json.load(f)

width = len(vector_field[0])
height = len(vector_field)

step_x, step_y = width / 10, height / 10
x = np.arange(step_x / 2, width, step_x, dtype=int)
y = np.arange(step_y / 2, height, step_y, dtype=int)
X, Y = np.meshgrid(x, y)

coords = [[(i, j) for i in x] for j in y]

Ex = []
Ey = []
for line in coords:
    x_vectors = []
    y_vectors = []
    for coord in line:
        x_vectors.append(vector_field[coord[1]][coord[0]][0])
        y_vectors.append(vector_field[coord[1]][coord[0]][1])
    Ex.append(x_vectors)
    Ey.append(y_vectors)
Ex = np.array(Ex)
Ey = np.array(Ey)

plt.figure(figsize=(10, 10))
plt.quiver(X, Y, Ex, Ey, color='k', scale=10)
# plt.ylim(len(vector_field), 0)
# plt.gca().invert_yaxis()
plt.show()

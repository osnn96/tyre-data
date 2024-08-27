import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Example data
FX = np.array([[-60.95], [-59.04], [-57.63]])
SA = np.array([[0.036], [0.085], [0.122]])

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(FX, SA, np.zeros_like(FX), c='b', marker='o')  # Z values are set to 0 for simplicity

# Set labels and title
ax.set_xlabel('FX (Longitudinal Force)')
ax.set_ylabel('SA (Slip Angle)')
ax.set_zlabel('Z Axis')
ax.set_title('3D Scatter Plot of FX and SA Data')

plt.show()

from scipy.io import loadmat
import matplotlib.pyplot as plt

# upload matlab file
data = loadmat(r"C:\Users\osman\OneDrive\Masaüstü\yazılımsal\codes\formula_student\tyre_data\B2356run18.mat")
print(data)
# belli variable için atama yap
data_variable = 'V'  # istediğin variable için değiştir burayı

plt.figure(figsize=(10, 6))
plt.plot(data[data_variable], color='blue', linestyle='-', marker='o', markersize=4, markerfacecolor='red', label=data_variable)
plt.title('Visualization of ' + data_variable, fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Value', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()

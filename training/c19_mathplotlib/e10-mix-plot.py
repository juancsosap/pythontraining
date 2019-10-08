import numpy as np
import matplotlib.pyplot as plt

# Generating original line
x = np.linspace(-10, 10, 30)
y = 5 * x + 50

# Generating line with errors
err = (np.random.random(x.shape) * 2 - 1) * 30
y_err = y + err

# Plot the data
plt.scatter(x, y, color='blue', alpha=0.4)
plt.scatter(x, y_err, color='orange', alpha=0.4)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')

# Plot the error difference
for i in range(30):
    plt.plot((x[i], x[i]), (y[i], y_err[i]), color='black')
    plt.scatter(x, y, color='black', s=5)
    plt.scatter(x, y_err, color='black', s=5)

plt.show()

# Calculating regression line
X = np.array([x, np.ones(x.shape)]).T

eq_template = 'y = {:,.2f} * x + {:,.2f}\n'

print('Original')
W_ori = np.linalg.inv(X.T @ X) @ X.T @ y
print(eq_template.format(*W_ori))

print('With Errors')
W_err = np.linalg.inv(X.T @ X) @ X.T @ y_err
print(eq_template.format(*W_err))

# Calculating predicted Y
y_pred = W_err[0] * x + W_err[1]
diff_err = y_err.T - y_pred

# Plot the data
plt.scatter(x, y, color='blue', alpha=0.4)
plt.scatter(x, y_err, color='orange', alpha=0.4)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')

# Plot the regression line
plt.plot(x, y_pred, color='red', alpha=0.5)

# Plot the error difference
for i in range(30):
    plt.plot((x[i], x[i]), (y_pred[i], y_err[i]), color='black')
    plt.scatter(x, y_pred, color='black', s=5)
    plt.scatter(x, y_err, color='black', s=5)

plt.show()

# Calculating regression error
rmse = (np.sum(diff_err ** 2) / x.shape[0]) ** (1/2)
print('Root Mean Square Error:', rmse)

diff_err_ori = y.T - y_pred
rmse_ori = (np.sum(diff_err_ori ** 2) / x.shape[0]) ** (1/2)
print('Root Mean Square Error:', rmse_ori)

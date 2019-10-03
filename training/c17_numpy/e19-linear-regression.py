import numpy as np

# Generating original line
x = np.linspace(-10, 10, 30)
y = 5 * x + 50

# Generating line with errors
err = (np.random.random(x.shape) * 2 - 1) * 30
y_err = y + err

# Printing data
template = " {x:<20} {y:<20} {err:<20} {y_err:<20}"
print(template.format(x = "X", y = "Y", err = "ERR", y_err = "Y ERR"))

for i in range(30):
    print(template.format(x = x[i], y = y[i], err = err[i], y_err = y_err[i]))

print()

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

# Printing regression predicted data
template = " {x:<20} {y:<20} {y_err:<20} {y_pred:<20} {err:<20}"
print(template.format(x = "X", y = "Y", y_err = "Y ERR", y_pred = "Y PRED", err = "DIFF ERR"))

for i in range(30):
    print(template.format(x = x[i], y = y[i], y_err = y_err[i], y_pred = y_pred[i], err = diff_err[i]))

print()

# Calculating regression error
rmse = (np.sum(diff_err ** 2) / x.shape[0]) ** (1/2)
print('Root Mean Square Error:', rmse)

diff_err_ori = y.T - y_pred
rmse_ori = (np.sum(diff_err_ori ** 2) / x.shape[0]) ** (1/2)
print('Root Mean Square Error:', rmse_ori)

import numpy as np

# Question 1

def f(x):
    z = x*np.sin(3*x)-np.exp(x)
    return z

def f_prime(x):
    z = np.sin(3*x) + 3*x*np.cos(3*x)-np.exp(x)
    return z

# First, use Newton-Raphson Method:

x = np.array([-1.6])
tol = 1e-6
num_iters1 = 0

for i in range(1000):

    # New Iteration:
    num_iters1 = num_iters1 + 1
    x = np.append(x, (x[i] - (f(x[i])/f_prime(x[i]))))

    # Check convergence:
    f_xi = np.abs(f(x[i]))
    
    if f_xi < tol:
        break
        
A1 = x


# Next, use bisection method:

x_left = -0.7
x_right = -0.4
tol = 1e-6

x_mid = np.array([(x_left + x_right)/2])
num_iters2 = 1

for j in range(1000):
    
    # Check convergence:
    f_xj = np.abs(f(x_mid[j]))

    if f_xj < tol:
        break

    else: # Proceed with another iteration
        num_iters2 = num_iters2 + 1
        
        if f(x_mid[j]) > 0:
            x_left = x_mid[j]

        else:
            x_right = x_mid[j]

        x_mid = np.append(x_mid, (x_left + x_right)/2)

A2 = x_mid
A3 = np.array([num_iters1, num_iters2])

# Question 2

A = np.array([[1, 2], [-1, 1]])
B = np.array([[2, 0], [0, 2]])
C = np.array([[2, 0, -3], [0, 0, -1]])
D = np.array([[1, 2], [2, 3], [-1, 0]])
x = np.array([1, 0])
y = np.array([0, 1])
z = np.array([1, 2, -1])

# Caluclate A + B:

A4 = A + B

# Calculate 3x - 4y:

A5 = 3*x - 4*y

# Calculate Ax:

A6 = np.dot(A,x)

# Calculate B(x - y):

A7 = np.dot(B, (x - y))

# Calculate Dx:

A8 = D @ x

# Calculate Dy + z:

A9 = (D @ y) + z

# Calculate AB:

A10 = np.dot(A,B)

# Calculate BC:

A11 = B @ C

# Calculate CD:

A12 = C @ D
# Scientific Computing 

## Introduction
This repository contains implementations of Linear ALgebra techniques and algorithms for matrix related computations in Python and NumPy : 
* Gaussian elimination and partial pivoting 
* Scaling a Linear System
* Perturbed Linear Systems 
* Least Squares fitting with Gram-Schmidt and QR
* Eigenvalue finding using:
  1. power iteration
  2. inverse ietration
  3. Rayleigh quotient iteration
  4. QR iteration
  5. Lanczos Iteration (Ritz values)
* Principal Component Analysis


## Repository Structure 
* Directory [Gaussian elimination](https://github.com/pankhuri22/Scientific-Computing-/tree/master/Gaussian%20elimination) contains scripts for
  1. Implementation of Gaussian Elimination on a matrix using No Pivoting
  2. Implementation of Gaussian Elimination on a matrix using Partial Pivoting
* [Scaling a Linear System](https://github.com/pankhuri22/Scientific-Computing-/tree/master/Scaling%20a%20Linear%20System) contains a script for scaling a linear system of the form Ax = b by a non singular diagonal matrix D to obtain a new system DAx = D. The script [Various_scaling](https://github.com/pankhuri22/Scientific-Computing-/blob/master/Scaling%20a%20Linear%20System/Various_scaling.py) contains code for scaling an existing system by 5 different types of diagonal matrix that are. : 
  1. D = I (Identity matrix)
  2. D = np.diag(2 * np.ones(n))
  3. D = np.diag(np.linspace(1, 100, 100))
  4. D = np.diag(np.linspace(1, 10000, 100))
  5. D = np.diag(2**-np.arange(-n//2, n//2, dtype=np.float64))
The final result is judged on the basis of 2-norm relative residuals, the relative error, and the condition number of the scaled matrices. High Relative Error means that the system is not accurate enough thus in (iii),(iv),(v) accuracy is not good where as in (i) and (ii) accuracy is good. condition no of matrix in (v) is almost 1 hence the matrix is well conditioned.
(iv) gives a very poor accuracy but the residual is very small in this case. Hence the system is ill-conditioned which can also be observed from the condition no of the matrix, that is pretty high.

* [Perturbed Linear Systems](https://github.com/pankhuri22/Scientific-Computing-/tree/master/Perturbed%20Linear%20Systems) 
contains script for computation of the linear system sensitivity analysis. It contains a plot for each b and perturbed b.
![plot](https://github.com/pankhuri22/Scientific-Computing-/blob/master/Perturbed%20Linear%20Systems/plot.png)

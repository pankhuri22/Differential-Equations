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
contains script for computation of the linear system sensitivity analysis, also it contains a plot for each b and perturbed b.
There can never be a point on the plot for which the vertical coordinate(thatis,∥δx∥/∥x∥) is larger than the horizontal coordinate (that is, cond(A)∥δb∥/∥b∥)because according to the inequality we have that vertical can never be larger than horizontal. also from the graph we can see that the y coordinates are very very small as compared to x coordinate and they can never be equal.
![plot](https://github.com/pankhuri22/Scientific-Computing-/blob/master/Perturbed%20Linear%20Systems/plot.png)

* [Power_iteration.py](https://github.com/pankhuri22/Scientific-Computing-/blob/master/Power_iteration.py) containts implementation of the power iteration method of finding eigen values and corresponding eigen vectors of a matrix. The resultant eigen value and eigen vector are : 
  1. eigen value. : 11.0
  2. eigen vector : array([0.5 , 1. , 0.75])

* The Directory [QR Factorization](https://github.com/pankhuri22/Scientific-Computing-/tree/master/QR%20Factorization) has: 
  1. Implementation of QR Factorization using Gram-Schmidt procedure
  2. Implementation of least square method to fit data to polynomials of degree 1 to 5 using Qr factorization and numpy.linalg.lstsq() method of NumPy. The results are as follows : 
  
|          |  A.shape |  Q.shape | R.shape |        Rel_error        |        A.cond       |        Q.cond       |        R.cond       |
|:--------:|:--------:|:--------:|:-------:|:-----------------------:|:-------------------:|:-------------------:|:-------------------:|
|   5 x 5  |   5 x 5  |   5 x 5  |  5 x 5  |  7.662753060 229763e-17 | 37.85837544 0617394 | 1.00000000 00000007 |  37.85837544 061737 |
|  10 x 10 |  10 x 10 |  10 x 10 | 10 x 10 | 1.078599527 1980571e-16 |  40.70365863 47463  | 1.00000000 00000022 | 40.70365863 4746354 |
| 100 x 80 | 100 x 80 | 100 x 80 | 80 x 80 | 2.882530633 2565366e-16 | 115.7470511 5977294 | 1.00000000 00000318 | 115.7470511 5977348 |

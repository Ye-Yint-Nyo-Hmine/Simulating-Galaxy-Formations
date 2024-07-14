import numpy as np
import matplotlib.pyplot as plt

def navier_stokes_equation(rho, v, P, mu, f):
    """
    Computes the Navier-Stokes equation for hydrodynamics.

    Parameters:
    rho : numpy array
        Density field.
    v : numpy array
        Velocity field. Should have shape (3, Nx, Ny, Nz) where 3 represents the vector components (x, y, z).
    P : numpy array
        Pressure field.
    mu : float
        Viscosity.
    f : numpy array
        External force field. Should have shape (3, Nx, Ny, Nz) where 3 represents the vector components (x, y, z).

    Returns:
    numpy array
        Acceleration field. Has the same shape as v.
    """

    # Calculate gradients and Laplacian
    grad_v = np.gradient(v)
    laplacian_v = np.sum(np.gradient(grad_v, axis=0), axis=0)  # Laplacian of v

    # Calculate acceleration field
    gradients = np.gradient(P)
    negated_gradients = [-x for x in gradients]
    acceleration = negated_gradients + mu * laplacian_v + f / rho

    return acceleration



if __name__ == '__main__':
    # Example usage
    Nx, Ny, Nz = 100, 100, 100  # Example dimensions
    rho = np.ones((Nx, Ny, Nz))  # Example density field
    v = np.zeros((3, Nx, Ny, Nz))  # Example velocity field (3 components)
    P = np.ones((Nx, Ny, Nz))  # Example pressure field
    mu = 0.01  # Example viscosity
    f = np.zeros((3, Nx, Ny, Nz))  # Example external force field (3 components)

    acceleration = navier_stokes_equation(rho, v, P, mu, f)
    print(acceleration.shape)  # Should print (3, Nx, Ny, Nz)


import numpy as np

def dark_matter_density(r, rho0, rs):
    """
    Compute the dark matter density using the NFW profile.
    
    Parameters:
    - r (float or numpy array): Radius at which to compute the density.
    - rho0 (float): Characteristic density of dark matter.
    - rs (float): Scale radius of the dark matter halo.
    
    Returns:
    - float or numpy array: Dark matter density at radius r.
    """
    x = r / rs
    return rho0 / (x * (1 + x)**2)


if __name__ == '__main__':
    # Example usage:
    radius = 10.0  # example radius
    rho0 = 1.0     # example characteristic density
    rs = 5.0       # example scale radius

    density = dark_matter_density(radius, rho0, rs)
    print(f"Dark matter density at r = {radius}: {density}")

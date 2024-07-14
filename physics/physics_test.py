import numpy as np
from dark_matter_distribution import dark_matter_density
from hydrodynamics import navier_stokes_equation
from n_body import n_body_simulation
from star_formation import calculate_star_formation_rate


# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
epsilon = 0.1    # Star formation efficiency
free_fall_time = 1.0  # Example value for free-fall time (t_ff)

# Initial conditions
# Example initial positions and masses
N = 0  # Number of particles
GAS_N = 100 # Number of gas particles
positions = np.random.uniform(-10, 10, size=(N, 3))
gas_positions = np.random.uniform(-10, 10, size=(GAS_N, 3))
masses = np.ones(N)  # Example masses (equal mass particles)

#! Note: Acceleration and movement calculations are commented out for now due to time complexity of performance
# TODO: Stars dying 
# TODO: Star dying -> forms more Gas paricles
# TODO: Dark matter density - > affects gas particles's formation of stars
# TODO: Later on, after creating visual, dark matter density messes with stars and gas particles's movement and acceleration
# TODO: Gas should interact with stars in positons and velocity,
# TODO: "Planets form from dust and gas that condense around a young star in a disk" if this process is seen, write an algorithm to detect it, then, create planets


# Example simulation loop
num_steps = 100000
dt = 0.1  # Time step

for step in range(num_steps):
    # Gravitational simulation
    #! accelerations = n_body_simulation(positions, masses, G)

    # Hydrodynamic simulation (example fields)
    rho = np.random.uniform(0.1, 1.0, size=(GAS_N,))
    v = np.random.uniform(-1, 1, size=(3, GAS_N))
    P = np.random.uniform(0.1, 1.0, size=(GAS_N,))
    mu = 0.01  # Example viscosity
    f = np.zeros_like(v)  # Example external force field

    #! acceleration_field = navier_stokes_equation(rho, v, P, mu, f)

    # Update positions and velocities
    #! gas_positions += dt * v.T  # Transpose v to match the shape of positions
    #! v += dt * acceleration_field

    # Calculate star formation rates
    star_formation_rates = calculate_star_formation_rate(rho, epsilon, free_fall_time)

    for star_formation_rate in range(int(np.sum(star_formation_rates))):
        new_position = np.array([[np.random.uniform(-10, 10), np.random.uniform(-10, 10), np.random.uniform(-10, 10)]])  # Example new position to add

        # Append the new position to the existing positions array
        positions = np.append(positions, new_position, axis=0)
        masses = np.append(masses, 1.0)
    
    
    stars = len(positions)
    
    
    # Calculate dark matter density
    # TODO: Add both stars and gas to the calculation of dark matter density
    r = np.linalg.norm(gas_positions, axis=1)  # Example radius calculation
    rho0 = 1.0  # Example characteristic density
    rs = 2.0   # Example scale radius
    dark_matter_densities = dark_matter_density(r, rho0, rs)


    # Print or store results (example)
    print(f"Step {step+1}: Mean gas density = {np.mean(rho)}, Mean star formation rate = {np.mean(star_formation_rates)}, Mean dark matter density = {np.mean(dark_matter_densities)}, Number of stars = {stars}")

# Additional steps: Visualization or analysis of simulation results

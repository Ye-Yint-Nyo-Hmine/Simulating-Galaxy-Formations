import numpy as np

def n_body_simulation(positions, masses, G):
    """
    Simulates the N-body gravitational interactions between particles.

    Parameters:
    positions (numpy.ndarray): Array of shape (N, 3) containing positions of particles.
    masses (numpy.ndarray): Array of shape (N,) containing masses of particles.
    G (float): Gravitational constant.

    Returns:
    numpy.ndarray: Array of accelerations (shape (N, 3)) for each particle.
    """
    N = len(positions)
    accelerations = np.zeros_like(positions, dtype=np.float64)  # Ensure accelerations are float

    for i in range(N):
        for j in range(N):
            if i != j:
                r_ij = positions[j] - positions[i]
                r_ij_norm = np.linalg.norm(r_ij)
                acceleration_i = G * masses[j] * r_ij / (r_ij_norm ** 3)
                accelerations[i] += acceleration_i

    return accelerations



if __name__ == '__main__':
    # Example usage:
    positions = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0]
    ])
    masses = np.array([10, 5, 3])
    G = 6.67430e-11  # Example gravitational constant in SI units

    accelerations = n_body_simulation(positions, masses, G)
    print("Accelerations:")
    print(accelerations)

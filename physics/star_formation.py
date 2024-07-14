def calculate_star_formation_rate(gas_density, star_formation_efficiency, free_fall_time):
    """
    Calculate the star formation rate based on empirical relations.

    Parameters:
    - gas_density: float, gas density (ρ)
    - star_formation_efficiency: float, star formation efficiency (ε)
    - free_fall_time: float, free-fall time (t_ff)

    Returns:
    - star_formation_rate: float, star formation rate (𝜌˙∗)
    """
    star_formation_rate = star_formation_efficiency * (gas_density / free_fall_time)
    return star_formation_rate


if __name__ == '__main__':
    # Example usage:
    gas_density = 10.0  # Example gas density
    star_formation_efficiency = 0.1  # Example star formation efficiency
    free_fall_time = 1.0  # Example free-fall time

    # Calculate star formation rate
    star_formation_rate = calculate_star_formation_rate(gas_density, star_formation_efficiency, free_fall_time)
    print(f"Star Formation Rate: {star_formation_rate} stars per unit time")

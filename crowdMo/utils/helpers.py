"""Module containing utility functions for the simulation."""

import numpy as np

def initialize_positions_and_velocities(num_individuals, room_size):
    """
    Randomly initialize positions and velocities of individuals.

    Args:
        num_individuals (int): Number of individuals in the simulation.
        room_size (int): Size of the room (square).

    Returns:
        numpy.ndarray: Initial positions.
        numpy.ndarray: Initial velocities.
    """
    positions = np.random.rand(num_individuals, 2) * room_size
    velocity = np.zeros((num_individuals, 2))
    return positions, velocity

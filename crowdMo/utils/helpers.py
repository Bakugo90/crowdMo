"""Module containing utility functions for the simulation."""

import numpy as np

#initialize positions and velocities randomly
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


#Helper function to calculate the direction force for an individual.
def calculate_direction_force(target_velocity, current_velocity, tau):
    """
    Calculate the direction force for an individual.

    Args:
        target_velocity (float): The target velocity.
        current_velocity (float): The current velocity of the individual.
        tau (float): Characteristic time of direction adjustment.

    Returns:
        float: Direction force.
    """
    force_direction = (target_velocity - current_velocity) / tau
    return force_direction

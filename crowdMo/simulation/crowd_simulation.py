"""Module for crowd behavior simulation."""

import numpy as np
import matplotlib.pyplot as plt

def calculate_direction_force(target_velocity, current_velocity, tau):
    """
    Calculate the direction force for each individual.

    Args:
        target_velocity (float): The target velocity.
        current_velocity (float): The current velocity of the individual.
        tau (float): Characteristic time of direction adjustment.

    Returns:
        float: Direction force.
    """
    direction_force = (target_velocity - current_velocity) / tau
    return direction_force

def update_positions(positions, velocity, num_individuals, exit_position, room_size, tau, repulsion_amp, repulsion_range, obstacle_amp, obstacle_range, obstacles):
    """
    Update positions and velocities of individuals in the simulation.

    Args:
        positions (numpy.ndarray): Current positions of individuals.
        velocity (numpy.ndarray): Current velocities of individuals.
        num_individuals (int): Number of individuals in the simulation.
        exit_position (tuple): Position of the exit.
        room_size (int): Size of the room (square).
        tau (float): Characteristic time of direction adjustment.
        repulsion_amp (float): Amplitude of repulsion force.
        repulsion_range (float): Range of repulsion force.
        obstacle_amp (float): Amplitude of obstacle force (increased).
        obstacle_range (float): Range of obstacle force (reduced).
        obstacles (list): List of obstacle positions and sizes.

    Returns:
        numpy.ndarray: New positions.
        numpy.ndarray: New velocities.
    """
    for i in range(num_individuals):
        # Calculate direction force
        target_vector = np.array(exit_position) - positions[i]
        direction_force = target_vector / np.linalg.norm(target_vector)

        # Calculate repulsion force with other individuals
        repulsion_force = np.zeros(2)
        for j in range(num_individuals):
            if i != j:
                distance = np.linalg.norm(positions[i] - positions[j])
                force_obstacle = repulsion_amp * np.exp(-distance / repulsion_range)
                repulsion_force += force_obstacle * (positions[i] - positions[j]) / distance

        # Calculate obstacle force with obstacles
        obstacle_force = np.zeros(2)
        for obstacle_position, obstacle_size in obstacles:
            distance_to_obstacle = np.linalg.norm(positions[i] - obstacle_position)
            if distance_to_obstacle < obstacle_size:
                obstacle_direction = (positions[i] - obstacle_position) / distance_to_obstacle
                obstacle_force += obstacle_amp * np.exp(-distance_to_obstacle / obstacle_range) * obstacle_direction

        # Update velocity and position
        velocity[i] = ((velocity[i] + tau * (direction_force + repulsion_force + obstacle_force)) / (1 + tau))
        positions[i] += velocity[i]

    return positions, velocity

def simulate_crowd_behavior(num_iterations, num_individuals, room_size, exit_position, obstacle_positions, obstacle_sizes, tau, repulsion_amp, repulsion_range, obstacle_amp, obstacle_range):
    """
    Simulate crowd behavior and visualize using matplotlib.

    Args:
        num_iterations (int): Number of simulation iterations.
        num_individuals (int): Number of individuals in the simulation.
        room_size (int): Size of the room (square).
        exit_position (tuple): Position of the exit.
        obstacle_positions (list): List of obstacle positions.
        obstacle_sizes (list): List of obstacle sizes.
        tau (float): Characteristic time of direction adjustment.
        repulsion_amp (float): Amplitude of repulsion force.
        repulsion_range (float): Range of repulsion force.
        obstacle_amp (float): Amplitude of obstacle force (increased).
        obstacle_range (float): Range of obstacle force (reduced).
    """
    positions = np.random.rand(num_individuals, 2) * room_size
    velocity = np.zeros((num_individuals, 2))

    plt.figure()

    for t in range(num_iterations):
        plt.clf()

        # Plot room
        plt.fill([0, room_size, room_size, 0], [0, 0, room_size, room_size], 'blue')

        # Plot obstacles
        for obstacle_position, obstacle_size in zip(obstacle_positions, obstacle_sizes):
            plt.gca().add_patch(plt.Circle(obstacle_position, obstacle_size, color='red'))

        # Plot individuals
        plt.plot(positions[:, 0], positions[:, 1], 'yo', markersize=8)

        # Plot exit
        plt.plot(exit_position[0], exit_position[1], 'go', markersize=10)

        plt.xlim(0, room_size)
        plt.ylim(0, room_size)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.pause(0.1)

        positions, velocity = update_positions(positions, velocity, num_individuals, exit_position, room_size, tau, repulsion_amp, repulsion_range, obstacle_amp, obstacle_range, zip(obstacle_positions, obstacle_sizes))

    plt.show()

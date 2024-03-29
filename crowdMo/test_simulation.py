"""Test script for crowd simulation."""

from crowdMo.simulation import crowd_simulation
from crowdMo.utils import helpers
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_individuals = 110  # Number of individuals in the room
room_size = 50  # Size of the room (square)
exit_position = (room_size // 2, room_size - 1)  # Exit position
tau = 0.1  # Characteristic time of direction adjustment
repulsion_amp = 1.0  # Amplitude of repulsion force
repulsion_range = 0.5  # Range of repulsion force
obstacle_amp = 10.0  # Amplitude of obstacle force (increased)
obstacle_range = 5.0  # Range of obstacle force (reduced)
obstacles = [((room_size // 4, room_size // 4), 3), ((3 * room_size // 4, room_size // 4), 3), ((room_size // 2, 3 * room_size // 4), 3)]  # List of obstacle positions and sizes

# Initialize positions and velocities
positions, velocity = helpers.initialize_positions_and_velocities(num_individuals, room_size)

temps_evacuation = []  # List to record evacuation time for each individual
densite_foule_obstacles = []  # List to record crowd density around obstacles

# Initialize figure for visualization
plt.figure()

# Main simulation loop
num_iterations = 100
for t in range(num_iterations):
    plt.clf()
    plt.fill([0, room_size, room_size, 0], [0, 0, room_size, room_size], 'blue')  # Display room in blue
    for obstacle_position, obstacle_size in obstacles:
        plt.gca().add_patch(plt.Circle(obstacle_position, obstacle_size, color='red'))  # Display obstacles in red

    plt.plot(positions[:, 0], positions[:, 1], 'yo', markersize=8)  # Display individuals in yellow
    plt.plot([exit_position[0] - 20 / 2, exit_position[0] + 20 / 2], [exit_position[1],  exit_position[1]], 'k-', linewidth=10)
    plt.plot(exit_position[0], exit_position[1], 'go', markersize=50)  # Display exit in green
    plt.plot([exit_position[0] - 50 / 2, exit_position[0] + 50 / 2], [exit_position[1],  exit_position[1]], 'g-', linewidth=10)
    plt.plot([exit_position[0] - 20 / 2, exit_position[0] - 20 / 2], [0, room_size], 'k-', linewidth=10)
    plt.plot([exit_position[0] + 20 / 2, exit_position[0] + 20 / 2], [0, room_size], 'k-', linewidth=10)
    plt.plot([exit_position[0] - 20 / 2, exit_position[0] + 20 / 2], [room_size - exit_position[1], room_size - exit_position[1]], 'k', linewidth=10)
    plt.xlim(0, room_size)
    plt.ylim(0, room_size)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.pause(0.1)  # Pause to display the figure

    # Update positions and velocities
    positions, velocity = crowd_simulation.update_positions(positions, velocity, num_individuals, exit_position, room_size, tau, repulsion_amp, repulsion_range, obstacle_amp, obstacle_range, obstacles)
     # Calculate and record evacuation time for each individual
    temps_evacuation_individus = [np.linalg.norm(pos - exit_position) for pos in positions]
    temps_evacuation.extend(temps_evacuation_individus)

    # Calculate and record crowd density around obstacles
    densite_obstacles = [sum(np.linalg.norm(pos - obs[0]) < obs[1] for pos in positions) for obs in obstacles]
    densite_foule_obstacles.append(sum(densite_obstacles) / (len(obstacles) * np.pi * sum(obs[1]**2 for obs in obstacles)))


temps_evacuation_moyen = np.mean(temps_evacuation)
densite_moyenne_foule_obstacles = np.mean(densite_foule_obstacles)

print("Average evacuation time for each individual : {:.2f}".format(temps_evacuation_moyen))
print("Average crowd density around obstacles : {:.2f}".format(densite_moyenne_foule_obstacles))

plt.show()

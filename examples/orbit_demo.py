import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import numpy as np
import matplotlib.pyplot as plt

from orbital_mechanics.simulator import (
    simulate_orbit,
    calculate_energy,
    calculate_angular_momentum
)


SUN_MASS = 1.989e30
EARTH_ORBIT_RADIUS = 1.496e11
G = 6.67430e-11

EARTH_ORBITAL_SPEED = np.sqrt(
    G * SUN_MASS / EARTH_ORBIT_RADIUS
)

initial_position = [
    EARTH_ORBIT_RADIUS,
    0
]

initial_velocity = [
    0,
    EARTH_ORBITAL_SPEED
]

times, positions, velocities = simulate_orbit(
    initial_position,
    initial_velocity,
    SUN_MASS,
    dt=86400,
    n_steps=365
)

energy = calculate_energy(
    positions,
    velocities,
    SUN_MASS
)

angular_momentum = calculate_angular_momentum(
    positions,
    velocities
)

x = positions[:, 0] / EARTH_ORBIT_RADIUS
y = positions[:, 1] / EARTH_ORBIT_RADIUS

time_years = times / (86400 * 365)

initial_energy = energy[0]

relative_energy_error = (
    (energy - initial_energy)
    / abs(initial_energy)
)

initial_angular_momentum = angular_momentum[0]

relative_angular_momentum_error = (
    (angular_momentum - initial_angular_momentum)
    / abs(initial_angular_momentum)
)

plt.figure(figsize=(8, 8))

plt.plot(
    x,
    y,
    label="Earth orbit"
)

plt.scatter(
    0,
    0,
    s=200,
    label="Sun"
)

plt.xlabel("x [AU]")
plt.ylabel("y [AU]")
plt.title("2D Earth–Sun Orbital Simulation")

plt.axis("equal")
plt.grid(True)
plt.legend()

plt.savefig(
    "earth_sun_orbit.png",
    dpi=300
)

plt.figure(figsize=(8, 5))

plt.plot(
    time_years,
    relative_energy_error
)

plt.xlabel("Time [years]")
plt.ylabel("Relative Energy Error")
plt.title("Orbital Energy Conservation")

plt.grid(True)

plt.savefig(
    "orbital_energy.png",
    dpi=300
)

plt.figure(figsize=(8, 5))

plt.plot(
    time_years,
    relative_angular_momentum_error
)

plt.xlabel("Time [years]")
plt.ylabel("Relative Angular Momentum Error")
plt.title("Angular Momentum Conservation")

plt.grid(True)

plt.savefig(
    "angular_momentum.png",
    dpi=300
)

print("Orbit saved as earth_sun_orbit.png")
print("Energy plot saved as orbital_energy.png")
print("Angular momentum plot saved as angular_momentum.png")
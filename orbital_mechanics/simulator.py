import numpy as np

G = 6.67430e-11


def gravitational_acceleration(position, central_mass):
    position = np.array(position, dtype=float)
    distance = np.linalg.norm(position)

    acceleration = -G * central_mass * position / distance**3

    return acceleration


def simulate_orbit(
    initial_position,
    initial_velocity,
    central_mass,
    dt=10.0,
    n_steps=10000
):
    position = np.array(initial_position, dtype=float)
    velocity = np.array(initial_velocity, dtype=float)

    positions = np.zeros((n_steps, 2))
    velocities = np.zeros((n_steps, 2))
    times = np.arange(n_steps) * dt

    acceleration = gravitational_acceleration(
        position,
        central_mass
    )

    for i in range(n_steps):

        positions[i] = position
        velocities[i] = velocity

        position = (
            position
            + velocity * dt
            + 0.5 * acceleration * dt**2
        )

        new_acceleration = gravitational_acceleration(
            position,
            central_mass
        )

        velocity = (
            velocity
            + 0.5 * (acceleration + new_acceleration) * dt
        )

        acceleration = new_acceleration

    return times, positions, velocities


def calculate_energy(
    positions,
    velocities,
    central_mass,
    object_mass=1.0
):
    distances = np.linalg.norm(positions, axis=1)
    speeds = np.linalg.norm(velocities, axis=1)

    kinetic_energy = (
        0.5 * object_mass * speeds**2
    )

    potential_energy = (
        -G * central_mass * object_mass / distances
    )

    total_energy = kinetic_energy + potential_energy

    return total_energy


def calculate_angular_momentum(
    positions,
    velocities,
    object_mass=1.0
):
    x = positions[:, 0]
    y = positions[:, 1]

    vx = velocities[:, 0]
    vy = velocities[:, 1]

    angular_momentum = (
        object_mass * (x * vy - y * vx)
    )

    return angular_momentum
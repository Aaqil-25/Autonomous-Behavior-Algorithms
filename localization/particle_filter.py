import numpy as np

def initialize_particles(num_particles, bounds):
    particles = np.random.uniform(bounds[0], bounds[1], size=(num_particles, 2))
    weights = np.ones(num_particles) / num_particles
    return particles, weights

def predict(particles, motion, noise_std):
    particles += motion + np.random.normal(0, noise_std, particles.shape)
    return particles

def update(particles, weights, measurement, landmarks, measurement_std):
    for i, landmark in enumerate(landmarks):
        distances = np.linalg.norm(particles - landmark, axis=1)
        weights *= np.exp(-0.5 * ((distances - measurement[i]) / measurement_std) ** 2)
    weights += 1e-300  # Avoid divide by zero
    weights /= sum(weights)
    return weights

def resample(particles, weights):
    indices = np.random.choice(len(particles), len(particles), p=weights)
    particles = particles[indices]
    weights.fill(1.0 / len(weights))
    return particles, weights

# Example usage
if __name__ == "__main__":
    num_particles = 100
    bounds = (0, 10)
    motion = np.array([0.5, 0.5])
    measurement = [5.0, 3.0]
    landmarks = [np.array([5, 5]), np.array([3, 3])]
    measurement_std = 0.5
    noise_std = 0.1

    particles, weights = initialize_particles(num_particles, bounds)
    particles = predict(particles, motion, noise_std)
    weights = update(particles, weights, measurement, landmarks, measurement_std)
    particles, weights = resample(particles, weights)
    print(f"Particles: {particles[:5]}")

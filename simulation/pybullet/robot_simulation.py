import pybullet as p
import pybullet_data
import time

def run_pybullet_simulation():
    """
    Runs a basic PyBullet simulation with a plane and a simple robot.
    """
    # Connect to PyBullet
    physics_client = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0, 0, -9.8)

    # Load a plane and a robot
    plane_id = p.loadURDF("plane.urdf")
    robot_id = p.loadURDF("r2d2.urdf", [0, 0, 1])

    print("Simulation started. Press Ctrl+C to stop.")
    
    # Run simulation
    try:
        for _ in range(10000):
            p.stepSimulation()
            time.sleep(1.0 / 240.0)
    except KeyboardInterrupt:
        print("Simulation stopped.")
    
    # Disconnect
    p.disconnect()

# Example usage
if __name__ == "__main__":
    run_pybullet_simulation()

import os
import subprocess

def launch_gazebo_simulation(world_file):
    """
    Launches a Gazebo simulation with the specified world file.
    
    :param world_file: Path to the Gazebo world file.
    """
    if not os.path.exists(world_file):
        raise FileNotFoundError(f"World file {world_file} not found.")

    try:
        print(f"Launching Gazebo simulation with world: {world_file}")
        subprocess.run(["gazebo", world_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch Gazebo: {e}")

# Example usage
if __name__ == "__main__":
    world_file = "path/to/your/world/file.world"  # Replace with actual path
    launch_gazebo_simulation(world_file)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def run(self):
        pass

class Selector(Node):
    def run(self):
        for child in self.children:
            if child.run():
                print(f"Selector node {self.name}: succeeded.")
                return True
        print(f"Selector node {self.name}: failed.")
        return False

class Sequence(Node):
    def run(self):
        for child in self.children:
            if not child.run():
                print(f"Sequence node {self.name}: failed.")
                return False
        print(f"Sequence node {self.name}: succeeded.")
        return True

class Task(Node):
    def __init__(self, name, func):
        super().__init__(name)
        self.func = func

    def run(self):
        result = self.func()
        print(f"Task {self.name}: {'succeeded' if result else 'failed'}.")
        return result

# Example usage
if __name__ == "__main__":
    def is_enemy_detected(): return True
    def attack(): return False
    def retreat(): return True

    root = Selector("Root")
    attack_sequence = Sequence("Attack Sequence")
    attack_sequence.add_child(Task("Detect Enemy", is_enemy_detected))
    attack_sequence.add_child(Task("Attack", attack))

    retreat_task = Task("Retreat", retreat)

    root.add_child(attack_sequence)
    root.add_child(retreat_task)

    root.run()

import pytest
from scripts.robot import Robot

class TestRobot:
    
    def setup_method(self):
        """Clear used names before each test"""
        Robot.used_names.clear()
    
    def test_robot_has_no_name_initially(self):
        robot = Robot()
        assert robot._name is None
    
    def test_robot_name_format(self):
        robot = Robot()
        name = robot.name
        assert len(name) == 5
        assert name[:2].isupper()
        assert name[:2].isalpha()
        assert name[2:].isdigit()
    
    def test_robot_name_is_persistent(self):
        robot = Robot()
        name1 = robot.name
        name2 = robot.name
        assert name1 == name2
    
    def test_different_robots_have_different_names(self):
        robot1 = Robot()
        robot2 = Robot()
        assert robot1.name != robot2.name
    
    def test_reset_clears_name(self):
        robot = Robot()
        old_name = robot.name
        robot.reset()
        assert robot._name is None
        # New name should be different after reset
        assert robot.name != old_name
    
    def test_reset_allows_name_reuse(self):
        robot1 = Robot()
        name = robot1.name
        robot1.reset()
        
        # Create many robots to potentially reuse the name
        robot2 = Robot()
        # The old name should no longer be in used_names
        assert name not in Robot.used_names or robot2.name == name
    
    def test_many_robots_have_unique_names(self):
        robots = [Robot() for _ in range(100)]
        names = [robot.name for robot in robots]
        assert len(set(names)) == len(names)  # All names are unique
    
    def test_used_names_tracking(self):
        Robot.used_names.clear()
        robot1 = Robot()
        robot2 = Robot()
        
        name1 = robot1.name
        name2 = robot2.name
        
        assert name1 in Robot.used_names
        assert name2 in Robot.used_names
        assert len(Robot.used_names) == 2
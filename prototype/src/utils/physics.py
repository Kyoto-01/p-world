from prototype.src.utils.geometry import Point
from prototype.src.utils.constants import *


def distance(pa: 'Point', pb: 'Point') -> int:  # in cells
    return int(((pb.x - pa.x)**2 + (pb.y - pa.y)**2)**(1 / 2))


def gforce(ma: 'float', mb: 'float', distance: 'int') -> float:  # in Newtons
    return (GRAVITATIONAL_CONSTANT * ma * mb) / (distance**2)


def acceleration_by_force(force: 'float', mass: 'float') -> float:  # in m/s**2
    return force / mass


def force_by_acceleration(acceleration: 'float', mass: 'float'):  # in Newtons
    return acceleration * mass

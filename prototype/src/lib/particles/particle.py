from threading import Thread
from uuid import uuid4

from prototype.src.utils.geometry import Point
from space import Space


class ParticleType:
    DEFAULT = 0
    DEFAULT_FERMION = 1
    DEFAULT_BOSON = 2
    GRAVITON_BOSON = 3
    FOTON_BOSON = 4


class Force:

    def __init__(
        self,
        up: 'float' = .0,
        right: 'float' = .0,
        down: 'float' = .0,
        left: 'float' = .0
    ):
        self.__up = up
        self.__right = right
        self.__down = down
        self.__left = left

    @property
    def up(self):
        return self.__up

    @property
    def right(self):
        return self.__right

    @property
    def down(self):
        return self.__down

    @property
    def left(self):
        return self.__left


class Particle(Thread):

    def __init__(
        self,
        mass: 'float',
        charge: 'float',
        spin: 'float',
        space: 'Space',
        type: 'ParticleType' = ParticleType.DEFAULT,
        posX: 'int' = 0,
        posY: 'int' = 0
    ):
        self.__id = str(uuid4())
        self.__mass = mass
        self.__charge = charge
        self.__spin = spin
        self.__space = space
        self.__type = type
        self.__position = Point(posX, posY)

        super.__init__()

    @property
    def id(self):
        return self.__id

    @property
    def mass(self):
        return self.__mass

    @property
    def charge(self):
        return self.__charge

    @property
    def spin(self):
        return self.__spin

    @property
    def space(self):
        return self.__space

    @property
    def type(self):
        return self.__type

    @property
    def position(self):
        return self.__position

    def get_current_cell(self):
        return self.__space.space[self.__position.y][self.__position.x]

    def move(self, posX: int, posY: int):
        cell = self.get_current_cell()

        if cell.particle is self:
            cell.reset()

        self.__position.x = posX
        self.__position.y = posY

        cell = self.get_current_cell()

        cell.put_particle(self)

    def recv_particle(self, p: 'Particle'):
        pass

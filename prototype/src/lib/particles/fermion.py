from time import sleep

import prototype.src.utils.physics as physics
from particle import Particle, ParticleType, Force
from graviton import Graviton
from space import Space


class Fermion(Particle):

    def __init__(
        self,
        mass: 'float',
        charge: 'float',
        spin: 'float',
        space: 'Space',
        type: 'ParticleType' = ParticleType.DEFAULT_FERMION,
        posX: 'int' = 0,
        posY: 'int' = 0
    ):
        self.__gforces = Force()

        super().__init__(mass, charge, spin, space, type, posX, posY)

    @property
    def gforces(self):
        return self.__gforces

    def __throw_graviton(self):
        Graviton(source=self).start()

    def __update_gforces(self, p: 'Graviton'):
        distance = physics.distance(self.position, p.srcParticle.position)
        gforce = physics.gforce(self.mass, p.srcParticle.mass, distance)

        moveX = p.memory['posx'] - self.__posX
        moveY = p.memory['posy'] - self.__posY

        if moveY < 0:
            self.__gforces.up = self.__apply_gravity(
                self.__gforces.up + gforce, moveX, moveY)
        elif moveY > 0:
            self.__gforces.down = self.__apply_gravity(
                self.__gforces.down + gforce, moveX, moveY)

        if moveX < 0:
            self.__gforces.left = self.__apply_gravity(
                self.__gforces.left + gforce, moveX, moveY)
        elif moveX > 0:
            self.__gforces.right = self.__apply_gravity(
                self.__gforces.right + gforce, moveX, moveY)

    def __apply_gravity(self, force: 'float', dirX: 'int', dirY: 'int'):
        while physics.acceleration_by_force(force, self.mass) >= physics.CELL_LEN:
            self.move(dirX, dirY)
            force -= physics.force_by_acceleration(physics.CELL_LEN, self.mass)

        return force

    def recv_particle(self, p: 'Particle'):
        if p.type == ParticleType.GRAVITON_BOSON:
            self.__update_gforces(p)
            self.__apply_gravity()

    def run(self):
        sleep(1 / self.space.gls)
        self.__throw_graviton()

from particle import Particle, ParticleType


class Boson(Particle):

    def __init__(
        self,
        mass: 'float',
        charge: 'float',
        spin: 'float',
        source: 'Particle',
        type: 'ParticleType' = ParticleType.DEFAULT_FERMION
    ):
        self.__srcParticle: 'Particle' = source
        self.__memory: 'dict' = {}

        super().__init__(mass, charge, spin, self.__srcParticle.space,
                         type, self.__srcParticle.position.x, self.__srcParticle.position.y)

    @property
    def srcParticle(self):
        return self.__srcParticle

    @property
    def memory(self):
        return self.__memory

    def _linear_movement(self, direction: 'str', sense: 'int', len: 'int'):
        if direction == 'x':
            for _ in range(len):
                self.move(self.position.x + sense, self.position.y)
        elif direction == 'y':
            for _ in range(len):
                self.move(self.position.x, self.position.y + sense)

    def _orbit(self):
        self._linear_movement('y', -1, (self.__space.ylen - self.position.y))

    def move(self, posX: int, posY: int):
        self.__memory['oldx'] = self.position.x
        self.__memory['oldy'] = self.position.y

        super().move(posX, posY)

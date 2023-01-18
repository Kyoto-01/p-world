from particle import Particle, ParticleType
from boson import Boson


class Graviton(Boson):

    MASS = 0.
    CHARGE = 0.
    SPIN = 2.

    def __init__(
        self,
        source: 'Particle',
        type: 'ParticleType' = ParticleType.GRAVITON_BOSON
    ):
        super().__init__(Graviton.MASS, Graviton.CHARGE, Graviton.SPIN, source, type)

    def _orbit(self):
        orbitLen = 0

        while ((self.posX != self.space.xlen) and (self.posY != self.space.ylen)):
            orbitLen += 2

            self._linear_movement('y', -1, 1)
            self._linear_movement('x', -1, orbitLen - 1)
            self._linear_movement('y', 1, orbitLen)
            self._linear_movement('x', 1, orbitLen)
            self._linear_movement('y', -1, orbitLen)

    def run(self):
        self._orbit()

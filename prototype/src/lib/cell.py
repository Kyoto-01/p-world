from particles.particle import Particle


class Cell:

    def __init__(self):
        self.__particle: 'Particle' = None

    @property
    def particle(self):
        return self.__particle

    def reset(self):
        self.__particle = None

    def put_particle(self, p: 'Particle'):
        if self.__particle:
            self.__particle.recv_particle(p)
        else:
            self.__particle = p

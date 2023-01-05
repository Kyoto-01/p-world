#include <space.h>

enum ParticleTypes {
    DEFAULT,
    DEFAULT_FERMION,
    DEFAULT_BOSON,
    GRAVITON_BOSON,
    FOTON_BOSON
}

class Particle {

    private:
        int id;
        Space space;
        float mass;
        float volume;
        int type;
        int posX;
        int posY;

    public:
        Particle(Space, float, float, char*, int, int);
        Particle(Space, float, float, char*);
        Particle(Space, float, float);

        void move();
};

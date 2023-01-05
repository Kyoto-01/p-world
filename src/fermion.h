#include <particle.h>

class Force {
    float up, right, down, left;
}

class Fermion : public Particle {
   private:
    Force gForces;

    void update_gforces(Particle p);
    void apply_gravity();
    void throw_graviton_pulse();

   public:
    Fermion(Space s, float mass, float vol, int type, int px, int py);
    Fermion(Space s, float mass, float vol, int type);
    Fermion(Space s, float mass, float vol);

    void receive_particle(Particle p);
}
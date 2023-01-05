#include <cell.h>

class Space {

    private:
        int xLen, yLen;
        int refreshTime; // in ms
        Cell *space[];

        void build_space();

    public:
        Space(int, int);
        Space(int, int, int);
};
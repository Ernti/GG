#ifndef CORE_H
#define CORE_H

#include <SDL.h>
#include "SDL_image.h"
#include <SDL_net.h>

class Core
{
    public:
        Core();
        virtual ~Core();

        void loop();
    protected:
    private:
};

#endif // CORE_H

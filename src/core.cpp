#include "core.h"

Core::Core()
{
    SDL_Init(SDL_INIT_EVERYTHING);
    IMG_Init(IMG_INIT_PNG);
    SDLNet_Init();
}

Core::~Core()
{
    IMG_Quit();
    SDL_Quit();
}

void Core::loop()
{

}

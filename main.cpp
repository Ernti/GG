#include "include/core.h"

int main(int argc, char** argv )
{
    Core* core = new Core;

    core->loop();

    delete core;

    return 0;
}

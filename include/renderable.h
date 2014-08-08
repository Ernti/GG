#ifndef RENDERABLE_H
#define RENDERABLE_H


class Renderable
{
    public:
        Renderable();
        virtual ~Renderable();
    protected:
    private:
        float x;
        float y;
        int tex;
};

#endif // RENDERABLE_H

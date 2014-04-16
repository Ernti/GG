'''
Created on 20 Feb 2014

@author: tore
'''


from OpenGL.GL import GL_TRIANGLES, GL_POLYGON, glVertexPointerf, glDrawElementsui, GL_VERTEX_ARRAY, glEnableClientState
import math
import numpy


class Engine(object):

    def __init__(self, data, ss):

        self.ss = ss
        self.type = data['type']
        self.thrust = data['thrust']
        self.mass = data['mass']

        self.vertex = numpy.array([numpy.array([0, 0.3, 0], 'f').reshape(1, 3),
                                   numpy.array([0, -0.3, 0], 'f').reshape(1, 3),
                                   numpy.array([-1.5, -0.5, 0], 'f').reshape(1, 3),
                                   numpy.array([-1.5, 0.5, 0], 'f').reshape(1, 3)])

        self.indices = numpy.arange(0, len(self.vertex), None, 'i')

    def render(self):

        vertex = []

        for vert, verts in enumerate(self.vertex):

            vx = numpy.dot(self.vertex[vert], numpy.array([math.cos(math.radians(self.ss.r)),
                                                                    math.sin(math.radians(self.ss.r)), 0,
                                                                    -math.sin(math.radians(self.ss.r)),
                                                                    math.cos(math.radians(self.ss.r)), 0,
                                                                    0, 0, 1], 'f').reshape(3, 3))

            vx = vx + numpy.array([self.ss.x + self.ss.ggci.player.x, self.ss.y + self.ss.ggci.player.y, 0 - self.ss.ggci.player.z], 'f').reshape(1, 3)

            vertex.append(vx)

        vertex = numpy.array(vertex, 'f').reshape(len(self.vertex), 3)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointerf(vertex)
        glDrawElementsui(GL_POLYGON, self.indices)
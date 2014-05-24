'''
Created on 13 May 2014

@author: tore
'''
import math
import numpy


class CollisionDetektor(object):

    def __init__(self, ggci):
        self.ggci = ggci

        for object in self.ggci.objectlist.objectlist:

            object.collisionbox = [0, 0, 0, 0]

            vertex = []
            for vert, verts in enumerate(object.vertex):
                vx = numpy.dot(object.vertex[vert], numpy.array([math.cos(math.radians(object.r)),
                                                                    math.sin(math.radians(object.r)), 0,
                                                                    -math.sin(math.radians(object.r)),
                                                                    math.cos(math.radians(object.r)), 0,
                                                                    0, 0, 1], 'f').reshape(3, 3))
                vertex.append(vx)
            vertex = numpy.array(vertex, 'f').reshape(len(object.vertex), 3)
            for vert in vertex:
                if vert[0] < object.collisionbox[0]:
                    object.collisionbox[0] = vert[0]
                if vert[0] > object.collisionbox[1]:
                    object.collisionbox[1] = vert[0]
                if vert[1] < object.collisionbox[2]:
                    object.collisionbox[2] = vert[1]
                if vert[1] > object.collisionbox[3]:
                    object.collisionbox[3] = vert[1]

            if object.type is 'ss':

                vertex = []
                for vert, verts in enumerate(object.engine.vertex):
                    vx = numpy.dot(object.engine.vertex[vert], numpy.array([math.cos(math.radians(object.r)),
                                                                    math.sin(math.radians(object.r)), 0,
                                                                    -math.sin(math.radians(object.r)),
                                                                    math.cos(math.radians(object.r)), 0,
                                                                    0, 0, 1], 'f').reshape(3, 3))
                    vertex.append(vx)
                vertex = numpy.array(vertex, 'f').reshape(len(vertex), 3)
                for vert in vertex:
                    if vert[0] < object.collisionbox[0]:
                        object.collisionbox[0] = vert[0]
                    if vert[0] > object.collisionbox[1]:
                        object.collisionbox[1] = vert[0]
                    if vert[1] < object.collisionbox[2]:
                        object.collisionbox[2] = vert[1]
                    if vert[1] > object.collisionbox[3]:
                        object.collisionbox[3] = vert[1]

        object = self.ggci.player.playership
        object.debug = False

        for obj in self.ggci.objectlist.objectlist:

            if object is not obj and object.type is 'ss':

                obj.debug = False

                if ((obj.collisionbox[0] + obj.x + self.ggci.player.x < object.collisionbox[0] + object.x + self.ggci.player.x < obj.collisionbox[1] + obj.x + self.ggci.player.x
                     and (obj.collisionbox[2] + obj.y + self.ggci.player.y < object.collisionbox[2] + object.y + self.ggci.player.y < obj.collisionbox[3] + obj.y + self.ggci.player.y
                          or obj.collisionbox[3] + obj.y + self.ggci.player.y > object.collisionbox[3] + object.y + self.ggci.player.y > obj.collisionbox[2] + obj.y + self.ggci.player.y))
                    or (obj.collisionbox[1] + obj.x + self.ggci.player.x > object.collisionbox[1] + object.x + self.ggci.player.x > obj.collisionbox[0] + obj.x + self.ggci.player.x
                        and (obj.collisionbox[2] + obj.y + self.ggci.player.y < object.collisionbox[2] + object.y + self.ggci.player.y < obj.collisionbox[3] + obj.y + self.ggci.player.y
                             or obj.collisionbox[3] + obj.y + self.ggci.player.y > object.collisionbox[3] + object.y + self.ggci.player.y > obj.collisionbox[2] + obj.y + self.ggci.player.y))):

                    obj.debug = True
                    object.debug = True

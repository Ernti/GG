'''
Created on 26 Jan 2014

@author: tore
'''

from OpenGL.GL import glVertex3f, glVertex2f


class ObjLoader:

    def __init__(self, path, out_vertices, out_uvs, out_normals):

        self.path = path
        self.out_vertices = out_vertices
        self.out_uvs = out_uvs
        self.out_normals = out_normals
        self.file = open(self.path, "r")
        self.temp_vertex = glVertex3f
        self.temp_uvs = glVertex2f

        if self.file == None:
            print("Impossible to open the file!")
            return False

        else:

            for line in self.file:

                i = line.split(" ")
                if i[0] == "v":

                    vertex = glVertex3f
                    vertex.x = i[1]
                    vertex.y = i[2]
                    vertex.z = i[3]

                    self.temp_vertices.append(vertex)

                elif i[0] == "vt":

                    uv = glVertex2f
                    uv.x = i[1]
                    uv.y = i[2]

                    self.temp_uvs.append(uv)

                elif i[0] == "vn":

                    normal = glVertex3f
                    normal.x = i[1]
                    normal.y = i[2]
                    normal.z = i[3]

                    self.temp_normals.append(normal)

                elif i[0] == "f":



                print(line)

            self.file.close()

            #while 1:

            #    lineHeader[128]
                 # read the first word of the line
            #    res = fscanf(file, "%s", lineHeader);
            #    if res == EOF:
            #        break # EOF = End Of File. Quit the loop.

                # else : parse lineHeader

            #    if strcmp( lineHeader, "v" ) == 0 ){
            #    glm::vec3 vertex;
            #    fscanf(file, "%f %f %f\n", &vertex.x, &vertex.y, &vertex.z );
            #    temp_vertices.push_back(vertex);
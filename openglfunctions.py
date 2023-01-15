from OpenGL.GL import *
from ctypes import c_void_p
def CopyToBuffer(pointer:int,size:int):
    glBufferData(GL_PIXEL_UNPACK_BUFFER, size,None, GL_STREAM_DRAW)
    data = glMapBuffer(GL_PIXEL_UNPACK_BUFFER,GL_WRITE_ONLY)
    array = (GLubyte*size).from_address(data)
    ctypes.memmove(array,pointer,size)
    glUnmapBuffer(GL_PIXEL_UNPACK_BUFFER)

def CreateTexture(pointer:int,size:tuple):
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_S,GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_WRAP_T,GL_CLAMP_TO_BORDER)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_BASE_LEVEL,0)
    glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAX_LEVEL,0)
    
    glTexImage2D(GL_TEXTURE_2D,0,GL_RGBA,size[0],size[1],0,GL_RGBA,GL_UNSIGNED_BYTE,c_void_p(pointer))

def UpdateTextureWithBuffer(pointer:int,size:int):
    glBufferData(GL_PIXEL_UNPACK_BUFFER, size, GL_STREAM_DRAW)
    data = glMapBuffer(GL_PIXEL_UNPACK_BUFFER,GL_WRITE_ONLY)
    array = (GLubyte*size).from_address(data)
    ctypes.memmove(array,pointer,size[0]*size[1]*4)
    glUnmapBuffer(GL_PIXEL_UNPACK_BUFFER)
    glTexSubImage2D(GL_TEXTURE_2D,0,0,0,size[0],size[1],GL_RGBA,GL_UNSIGNED_BYTE,c_void_p(0))
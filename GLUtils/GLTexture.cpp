#ifdef __linux__
// use native glew.h on linux
#include <GL/glew.h>
#else
#include <Include/glew.h>
#endif

#include "GLTexture.h"
#include <Utils/BMPIO.h>
#include <Utils/Image.h>
#include <Utils/Utils.h>

#ifdef _WIN32
#ifndef GL_TEXTURE_MAX_ANISOTROPY_EXT
#define GL_TEXTURE_MAX_ANISOTROPY_EXT 0x84FE
#endif
#ifndef GL_MAX_TEXTURE_MAX_ANISOTROPY
#define GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT 0x84FF
#endif
#endif // _WIN32

/**
	This method checks the int value that is passed in as a parameter, and returns true if it is one of
	64, 128, 256 or 512, false otherwise
*/
bool checkTexSize(int x){
	return (x == 64 || x == 128 || x == 256 || x == 512 || x == 1024 || x ==2048);
}


/*
	The constructor takes as input the name of a .bmp file that contains the texture to be loaded.
	This constructor throws errors if the file cannot be found, or if it's height and width are not powers of 2
*/
GLTexture::GLTexture(const char* fileName){
	//load the image
	BMPIO b(fileName);
	Image* im = b.loadFromFile();

	texID = 0;

	//and generate the texture...
	glGenTextures(1, &texID);

	activate();

	if (!checkTexSize(im->getWidth()) || !checkTexSize(im->getHeight()) || im->getNrBytes()!=3){
		throwError("Wrong texture dimension or nr bits in file \'%s\'", fileName);
	}

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR);

    GLfloat value, max_anisotropy = 4.0f; /* don't exceed this value...*/
    glGetFloatv(GL_MAX_TEXTURE_MAX_ANISOTROPY_EXT, &value);

    value = (value > max_anisotropy) ? max_anisotropy : value;
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAX_ANISOTROPY_EXT, value);

	//glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_LINEAR);
	//glTexParameteri(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_LINEAR);
	//glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, im->getWidth(), im->getHeight(), 0, GL_RGB, GL_UNSIGNED_BYTE, im->getDataPointer());
    //glGenerateMipmap(GL_TEXTURE_2D);

	GLint ires = gluBuild2DMipmaps(GL_TEXTURE_2D, 3, im->getWidth(), im->getHeight(), GL_RGB, GL_UNSIGNED_BYTE, im->getDataPointer());

    if ( ires != 0 ) {
       throwError("GLUtils.GLTexture::GLTexture:  gluBuild2DMipmaps() returns %d\n", ires);
    }

	delete im;
}


/*
	Destructor...
*/
GLTexture::~GLTexture(void){
	glDeleteTextures(1, &texID);
}


/*
	this method sets the current texture as the active
*/
void GLTexture::activate(){
	glBindTexture(GL_TEXTURE_2D, texID);
}



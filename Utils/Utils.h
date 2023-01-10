#pragma once

#include <stdarg.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdexcept>

#if defined(_MSC_VER)
#pragma warning (push)
#pragma warning (disable : 4275 4251)
#endif

#include <vector>

#if defined(_MSC_VER)
#pragma warning (pop)
#endif

#include <Utils/UtilsDll.h>

#define DynamicArray std::vector

typedef unsigned int uint;

// Define a prototype to a generic output function
// It can be overriden in python to print to a log file, for example

// the same function with vargs
#ifndef CW_SWIG_INCLUDE
  UTILS_DECLSPEC
  int tprintf(const char *format, ...);
  UTILS_DECLSPEC
  int tvprintf(const char *format, va_list ap);
#else
  %{
  extern int tprintf(const char *format, ...);
  extern int tvprintf(const char *format, va_list ap);
  %}
#endif
UTILS_DECLSPEC
void test(void);

/**
	This method throws an error with a specified text and arguments
*/
UTILS_DECLSPEC
inline void throwError(const char *fmt, ...){		// Custom error creation method

	char		text[256];								// Holds Our String
	va_list		ap;										// Pointer To List Of Arguments

	if (fmt == NULL)									// If There's No Text
		return;											// Do Nothing

	va_start(ap, fmt);									// Parses The String For Variables
    vsprintf(text, fmt, ap);						    // And Converts Symbols To Actual Numbers
	va_end(ap);											// Results Are Stored In Text

	tprintf( text );
	throw std::runtime_error(text);
}

/**
	This method reads all the doubles from the given file and stores them in the array of doubles that is passed in
*/
UTILS_DECLSPEC
inline void readDoublesFromFile(FILE* f, DynamicArray<double> *d){
	double temp;
	while (fscanf(f, "%lf\n", &temp) == 1)
		d->push_back(temp);
}

/**
	This method returns a pointer to the first non-white space character location in the provided buffer
*/
UTILS_DECLSPEC
inline char* lTrim(char* buffer){
	while (*buffer==' ' || *buffer=='\t' || *buffer=='\n' || *buffer=='\r')
		buffer++;
	return buffer;
}

UTILS_DECLSPEC
inline char* rTrim(char* buffer){
	int index = (int)strlen(buffer) - 1;
	while (index>=0){
		if (buffer[index]==' ' || buffer[index]=='\t' || buffer[index]=='\n' || buffer[index]=='\r'){
			buffer[index] = '\0';
			index--;
		}
		else
			break;
	}
	return buffer;
}

UTILS_DECLSPEC
inline char* trim(char* buffer){
	return rTrim(lTrim(buffer));
}

/**
	This method reads a line from a file. It does not return empty lines or ones that start with a pound key - those are assumed to be comments.
	This method returns true if a line is read, false otherwise (for instance the end of file is met).
*/
UTILS_DECLSPEC
inline bool readValidLine(char* line, FILE* fp){
	while (!feof(fp)){
		char* cp = fgets(line, 100, fp);
		char* tmp = trim(line);
		if (tmp[0]!='#' && tmp[0]!='\0')
			return true;
	}

	return false;
}

/**
	This method returns a DynamicArray of char pointers that correspond to the addressed
	of the tokens that are separated by white space in the string that is passed in as a pointer.
*/
UTILS_DECLSPEC
inline DynamicArray<char*> getTokens(char* input){
	DynamicArray<char*> result;
	input = lTrim(input);
	//read in the strings one by one - assume that each tokens are less than 100 chars in length
	while (input[0]!='\0'){
		result.push_back(input);
		char tempStr[100];
		sscanf(input, "%s", tempStr);
		input = lTrim(input + strlen(tempStr));
	}
	return result;
}

#define __max__(x,y) (((x)>(y))?(x):(y))

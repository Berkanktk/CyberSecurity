# Common C functions in assembly
## printf
The printf function is used to print to the standard output. It is defined in the stdio.h header file. The printf function is a variadic function which means that it can take a variable number of arguments. The printf function is defined as follows:
```c
int printf(const char *format, ...);
```

The printf function takes a format string as its first argument and the rest of the arguments are the values to be printed. The format string is a string that contains the text to be printed and the format specifiers which are used to specify the type of the values to be printed. The format specifiers are the following:

| Format Specifier | Description |
|---|---|
| %c | Character |
| %d | Signed decimal integer |
| %e | Scientific notation |
| %f | Decimal floating point |
| %g | Use the shortest representation: %e or %f |
| %i | Signed decimal integer |
| %o | Unsigned octal |
| %s | String of characters |
| %u | Unsigned decimal integer |
| %x | Unsigned hexadecimal integer |
| %X | Unsigned hexadecimal integer (uppercase) |

The printf function returns the number of characters printed. If an error occurs, it returns a negative number.

## scanf
The scanf function is used to read from the standard input. It is defined in the stdio.h header file. The scanf function is also a variadic function which means that it can take a variable number of arguments. The scanf function is defined as follows:
```c
int scanf(const char *format, ...);
```

The scanf function takes a format string as its first argument and the rest of the arguments are the variables to be read. The format string is a string that contains the text to be read and the format specifiers which are used to specify the type of the values to be read. The format specifiers are the same as the printf function.

The scanf function returns the number of input items assigned. If the reading fails, it returns EOF.

## strlen
The strlen function is used to find the length of a string. It is defined in the string.h header file. The strlen function is defined as follows:
```c
size_t strlen(const char *s);
```

The strlen function takes a string as its argument and returns the length of the string. The length of the string is the number of characters in the string excluding the null character.

## strcpy
The strcpy function is used to copy a string. It is defined in the string.h header file. The strcpy function is defined as follows:
```c
char *strcpy(char *dest, const char *src);
```

The strcpy function takes two strings as its arguments. The first argument is the destination string and the second argument is the source string. The strcpy function copies the source string to the destination string and returns the destination string.

## strcat
The strcat function is used to concatenate two strings. It is defined in the string.h header file. The strcat function is defined as follows:
```c
char *strcat(char *dest, const char *src);
```

The strcat function takes two strings as its arguments. The first argument is the destination string and the second argument is the source string. The strcat function concatenates the source string to the destination string and returns the destination string.

## strcmp
The strcmp function is used to compare two strings. It is defined in the string.h header file. The strcmp function is defined as follows:
```c
int strcmp(const char *s1, const char *s2);
```

The strcmp function takes two strings as its arguments. The first argument is the first string and the second argument is the second string. The strcmp function compares the two strings and returns an integer less than, equal to, or greater than zero if the first string is found, respectively, to be less than, to match, or be greater than the second string.

## atoi
The atoi function is used to convert a string to an integer. It is defined in the stdlib.h header file. The atoi function is defined as follows:
```c
int atoi(const char *nptr);
```

The atoi function takes a string as its argument and returns the integer value of the string. The string must contain a valid integer number. If the string does not contain a valid integer number, the atoi function returns zero.

## malloc
The malloc function is used to dynamically allocate memory. It is defined in the stdlib.h header file. The malloc function is defined as follows:
```c
void *malloc(size_t size);
```

The malloc function takes the size of the memory to be allocated as its argument and returns a pointer to the allocated memory. The allocated memory is uninitialized. If the memory cannot be allocated, the malloc function returns a null pointer.

## free
The free function is used to free the memory allocated by malloc. It is defined in the stdlib.h header file. The free function is defined as follows:
```c
void free(void *ptr);
```

The free function takes a pointer to the memory to be freed as its argument and returns nothing. The free function does not return any value.

# strcmp
The strcmp function is used to compare two strings. It is defined in the string.h header file. The strcmp function is defined as follows:
```c
int strcmp(const char *s1, const char *s2);
```

The strcmp function takes two strings as its arguments. The first argument is the first string and the second argument is the second string. The strcmp function compares the two strings and returns an integer less than, equal to, or greater than zero if the first string is found, respectively, to be less than, to match, or be greater than the second string.

# strncmp 
The strncmp function is used to compare two strings. It is defined in the string.h header file. The strncmp function is defined as follows:
```c
int strncmp(const char *s1, const char *s2, size_t n);
```

The strncmp function takes three arguments. The first argument is the first string, the second argument is the second string, and the third argument is the number of characters to be compared. The strncmp function compares the two strings and returns an integer less than, equal to, or greater than zero if the first string is found, respectively, to be less than, to match, or be greater than the second string.

# puts
The puts function is used to print a string to the standard output followed by a newline character. It is defined in the stdio.h header file. The puts function is defined as follows:
```c
int puts(const char *s);
```
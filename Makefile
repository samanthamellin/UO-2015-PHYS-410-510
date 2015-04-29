#
# this is a comment

#
# define environment variables (compilers/linker/libraries...)

CC = gcc

#
# define targets

all: hello

hello.o: hello.c
	$(CC) -c hello.c -o hello.o

hello: hello.o
	$(CC) -o hello hello.o

# run tests
check:

clean:
	rm -f hello.o hello


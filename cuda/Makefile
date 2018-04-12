# macros
CC = g++
NVCC = nvcc
# Changes to file made to work with conda installed cppunit
# CFLAGS = -c -Wall -g -I/opt/local/include -I$(HOME)/cppunit/include 
# LDFLAGS = -L/opt/local/lib -L$(HOME)/cppunit/lib 
CFLAGS = -c -Wall -g -I/opt/local/include -I$(HOME)/miniconda3/pkgs/cppunit-1.13.2-0/include/
LDFLAGS = -L/opt/local/lib -L$(HOME)/miniconda3/pkgs/cppunit-1.13.2-0/lib
SOURCES = driver.cpp seamcarver.cu image.cpp energies.cu
OBJECTS = driver.o seamcarver.o image.o energies.o
LIBS = -lcppunit -ldl
EXECUTABLE = driver.out

# targets
all: $(SOURCES) $(EXECUTABLE)


$(EXECUTABLE): $(OBJECTS)
	$(NVCC) $(LDFLAGS) $(OBJECTS) -o $@ $(LIBS)

  
%.o : %.cu %.h
	$(NVCC) -c $< -o $@
  
  
.cpp.o:
	$(CC) $(CFLAGS) $< -o $@


# clean
clean:
	rm -f $(EXECUTABLE) $(OBJECTS)

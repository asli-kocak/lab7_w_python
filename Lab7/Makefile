LAB       = lab7

BREWPATH  = $(shell brew --prefix)
CXX       = $(shell fltk-config --cxx) 
CXXFLAGS  = $(shell fltk-config --cxxflags) -std=c++11 -D_CRT_SECURE_NO_WARNINGS -DGL_SILENCE_DEPRECATION -Wno-macro-redefined -I$(BREWPATH)/include
LDFLAGS   = $(shell fltk-config --ldflags --use-gl --use-images) -L$(BREWPATH)/lib
   
POSTBUILD = fltk-config --post # build .app folder for osx. (does nothing on pc)

$(LAB): % : main.o MyGLCanvas.o ply.o ppm.o SceneObject.o ShaderManager.o 
	$(CXX) $(LDFLAGS) $^ -o $@
	$(POSTBUILD) $@

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

clean:
	rm -rf $(LAB) $(LAB).app *.o *~ *.dSYM


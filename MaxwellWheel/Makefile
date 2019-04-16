ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/plot.pdf

# hier Python-Skripte:
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python new.py

# hier Python-Skripte:
#build/example.pdf: example.py matplotlibrc header-matplotlib.tex | build
#	TEXINPUTS="$(call translate,$(pwd):)" python example.py

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean

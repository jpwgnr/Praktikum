ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/Stange3a.pdf build/Stange3b.pdf

# hier Python-Skripte:
build/Stange3a.pdf: getE1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python getE1.py

build/Stange3b.pdf: getE2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python getE2.py
build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean

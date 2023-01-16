# Modular Make - top level makefile
PROJPATH = $(PWD)
PROJNAME = $(notdir $(PROJPATH))

MK = ~/_mk

include $(wildcard $(MK)/*.mk)
TARGET: $(PROJNAME)

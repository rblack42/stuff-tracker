# Modular Make - top level makefile
PROJPATH = $(PWD)
PROJNAME = $(notdir $(PROJPATH))
APPNAME = stuff_tracker
MK = ~/_mk

include $(wildcard $(MK)/*.mk)
TARGET: $(APPNAME)

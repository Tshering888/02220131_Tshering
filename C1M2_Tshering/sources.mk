# sources.mk
# Defines platform-specific sources and include directories

ifeq ($(PLATFORM),HOST)
    # Host platform sources
    SOURCES = src/main.c \
              src/memory.c

    # Include directories
    INCLUDES = -Iinclude/common

else ifeq ($(PLATFORM),MSP432)
    # MSP432 platform sources
    SOURCES = src/main.c \
              src/memory.c \
              src/interrupts_msp432p401r_gcc.c \
              src/startup_msp432p401r_gcc.c \
              src/system_msp432p401r.c

    # Include directories
    INCLUDES = -Iinclude/common -Iinclude/msp432 -Iinclude/CMSIS
endif
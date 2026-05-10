# Makefile for C1M2 Assignment
# Supports HOST and MSP432 builds
# Generates preprocessed, assembly, object files, map, and executable

# Include sources and includes
include sources.mk

# ======================
# Platform-specific compiler and flags
# ======================
ifeq ($(PLATFORM),HOST)
    CC = gcc
    CFLAGS = -Wall -Werror -g -O0 -std=c99 -DHOST
    LDFLAGS = 
else ifeq ($(PLATFORM),MSP432)
    CC = arm-none-eabi-gcc
    CFLAGS = -Wall -Werror -g -O0 -std=c99 -DMSP432 \
             -mcpu=cortex-m4 -mthumb -march=armv7e-m \
             -mfloat-abi=hard -mfpu=fpv4-sp-d16
    LDFLAGS = -T msp432p401r.lds --specs=nosys.specs
endif

# Include directories
CPPFLAGS = $(INCLUDES)

# Output executable
OUTPUT = c1m2.out

# Object and dependency files
OBJ = $(SOURCES:.c=.o)
DEP = $(SOURCES:.c=.d)

# ======================
# PHONY targets
# ======================
.PHONY: all build compile-all clean

# ======================
# Default target
# ======================
all: build

# ======================
# Preprocessed files
# ======================
%.i: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -E $< -o $@

# ======================
# Assembly files
# ======================
%.asm: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -S $< -o $@

# Full project assembly dump
project.asm: $(OUTPUT)
	objdump -d $(OUTPUT) > project.asm

# ======================
# Object files with dependency generation
# ======================
%.o: %.c
	$(CC) $(CPPFLAGS) $(CFLAGS) -c $< -o $@ -MMD -MP

# ======================
# Compile all objects without linking
# ======================
compile-all: $(OBJ)
	@echo "All object files compiled."

# ======================
# Build final executable
# ======================
build: $(OBJ)
	$(CC) $(OBJ) $(LDFLAGS) -o $(OUTPUT) -Wl,-Map=c1m2.map
	@echo "Build complete. Code size:"
	size $(OUTPUT)

# ======================
# Clean all build outputs
# ======================
clean:
	rm -f $(OBJ) $(DEP) *.i *.asm $(OUTPUT) c1m2.map project.asm
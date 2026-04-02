# Challenge: GPIO Register Control with Bit Manipulation

**Topic:** embedded-programming > c-fundamentals  
**Level:** beginner  
**Date:** 2026-04-01  
**Sources:** [EmbeddedPrep](https://embeddedprep.com/structure-with-pointers/), [E-Skills Bitwise Operations](https://www.ewskills.com/embedded-c/bitwise-operations), [Electronics Hub Bitwise Operators](https://www.electronicshub.org/bitwise-operators-in-microcontroller-programming/)

## Problem

You're working with a hypothetical microcontroller that has a GPIO control register at address `0x40000000`. This register controls 8 pins (bits 0-7). Each bit represents a pin: 1 = pin ON, 0 = pin OFF.

Your task: Write C code that manipulates this register to:
1. Set pin 2 to ON
2. Set pin 5 to ON
3. Check if pin 3 is currently ON
4. Clear pin 7 (turn it OFF)
5. Toggle pin 1 (flip its current state)

## Requirements

- [ ] Use a volatile pointer to access the GPIO register
- [ ] Use bitwise operations (OR, AND, XOR) appropriately
- [ ] Each operation must use a single line of code (one statement per operation)
- [ ] Code compiles without warnings
- [ ] Explain what each operation does in comments

## Starter Code

```c
#include <stdint.h>
#include <stdio.h>

// GPIO register at fixed address
volatile uint8_t *gpio_register = (uint8_t *)0x40000000;

int main() {
    // Initialize register to a known state (0x00 = all pins OFF)
    *gpio_register = 0x00;
    
    // TODO: Add your code here
    // 1. Set pin 2 to ON (bit 2 = 1)
    
    // 2. Set pin 5 to ON (bit 5 = 1)
    
    // 3. Check if pin 3 is ON and print result
    
    // 4. Clear pin 7 (bit 7 = 0)
    
    // 5. Toggle pin 1 (flip its current state)
    
    // Print final register state
    printf("Final GPIO register value: 0x%02X\n", *gpio_register);
    printf("Binary: ");
    for (int i = 7; i >= 0; i--) {
        printf("%d", (*gpio_register >> i) & 1);
    }
    printf("\n");
    
    return 0;
}
```

## Acceptance Criteria

Your solution must:
1. Compile without errors or warnings (`gcc -Wall -Wextra`)
2. Use correct bitwise operations for each task:
   - **Set bit:** use OR with mask `(1 << position)`
   - **Check bit:** use AND with mask and compare
   - **Clear bit:** use AND with inverted mask `~(1 << position)`
   - **Toggle bit:** use XOR with mask `(1 << position)`
3. Include comments explaining each operation
4. When run, print the final register state showing which pins are ON

## Solution File

Write your solution in: `challenges/embedded-programming/c-fundamentals-001-solution.c`

Compile and test locally, then paste the code into that file when ready.

#include <stdint.h>
#include <stdio.h>

// GPIO register at fixed address
volatile uint8_t *gpio_register = (uint8_t *)0x40004000;

int main() {
    // Initialize register to a known state (0x00 = all pins OFF)
    *gpio_register = 0x00;

    // 1. Set pin 2 to ON — OR with mask sets bit 2
    *gpio_register |= (1 << 2);

    // 2. Set pin 5 to ON — OR with mask sets bit 5
    *gpio_register |= (1 << 5);

    // 3. Check if pin 3 is ON — AND with mask isolates bit 3
    if (*gpio_register & (1 << 3)) {
        printf("Pin 3 is ON\n");
    } else {
        printf("Pin 3 is OFF\n");
    }

    // 4. Clear pin 7 — AND with inverted mask clears bit 7
    *gpio_register &= ~(1 << 7);

    // 5. Toggle pin 1 — XOR with mask flips bit 1
    *gpio_register ^= (1 << 1);

    // Print final register state
    printf("Final GPIO register value: 0x%02X\n", *gpio_register);
    printf("Binary: ");
    for (int i = 7; i >= 0; i--) {
        printf("%d", (*gpio_register >> i) & 1);
    }
    printf("\n");

    return 0;
}

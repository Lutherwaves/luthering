# C Fundamentals Practice — Web Dev → Embedded Bridge

**Topic:** embedded-programming > c-fundamentals
**Level:** beginner
**Date:** 2026-04-05

---

## Exercise 1: Variables Live in Memory (warm-up)

In JS, you never think about where `let x = 5` lives. In C, every variable has an address.

```c
#include <stdio.h>

int main() {
    int temperature = 72;
    int humidity = 45;

    // TODO: Print the VALUE of each variable
    // TODO: Print the ADDRESS of each variable using &
    // Hint: use %d for value, %p for address
    // Example: printf("temp value: %d\n", temperature);
    // Example: printf("temp address: %p\n", &temperature);

    return 0;
}
```

**Your task:** Fill in the TODOs. Compile with `gcc -o ex1 ex1.c && ./ex1`

**Web dev analogy:** Think of `&temperature` like a database row ID — it tells you WHERE the data lives, not what the data IS.

---

## Exercise 2: Pointers = References You Can See

In JS: `const obj = { val: 5 }` — obj is already a reference.
In C: you choose explicitly whether to work with values or references.

```c
#include <stdio.h>

int main() {
    int sensor_reading = 100;
    int *ptr = &sensor_reading;  // ptr "points to" sensor_reading

    printf("Value directly: %d\n", sensor_reading);
    printf("Value via pointer: %d\n", *ptr);  // * = "go to that address"

    // TODO: Change sensor_reading to 200 using the POINTER (not the variable)
    // Hint: *ptr = ???

    printf("New value: %d\n", sensor_reading);  // Should print 200

    return 0;
}
```

**Your task:** Write one line to change the value through the pointer.

**Web dev analogy:** Like updating a database record by ID instead of by value.

---

## Exercise 3: Structs = Objects Without Methods

In JS you have `{ name: "sensor", value: 42 }`. C has structs — same idea, no methods.

```c
#include <stdio.h>

// This is like a TypeScript interface
typedef struct {
    char name[20];
    int value;
    int is_active;  // C has no booleans — 0 = false, non-zero = true
} Sensor;

int main() {
    // TODO: Create a Sensor called "thermostat" with value 72, active
    // Hint: Sensor s = {"thermostat", 72, 1};

    // TODO: Print all three fields
    // Hint: printf("Name: %s\n", s.name);

    // TODO: Change the value to 68 (like s.value = 68)

    // TODO: Print the updated value

    return 0;
}
```

**Web dev analogy:** `typedef struct` ≈ TypeScript `interface`. Access with `.` just like JS objects.

---

## Exercise 4: Flags with Bitwise Ops (the practical one)

In web dev, you use booleans: `{ isAdmin: true, canEdit: true, canDelete: false }`.
In embedded, you pack multiple flags into ONE byte to save memory:

```
Bit 0 = isActive
Bit 1 = isAdmin
Bit 2 = canRead
Bit 3 = canWrite
Bit 4 = canDelete
```

```c
#include <stdio.h>
#include <stdint.h>

#define IS_ACTIVE  (1 << 0)  // 00000001
#define IS_ADMIN   (1 << 1)  // 00000010
#define CAN_READ   (1 << 2)  // 00000100
#define CAN_WRITE  (1 << 3)  // 00001000
#define CAN_DELETE  (1 << 4)  // 00010000

int main() {
    uint8_t permissions = 0;  // Start with no permissions

    // TODO 1: Make user active and give read permission
    //         (set IS_ACTIVE and CAN_READ bits)

    // TODO 2: Promote to admin (set IS_ADMIN bit)

    // TODO 3: Check if user can write — print yes or no

    // TODO 4: Give write permission

    // TODO 5: Revoke delete permission (clear CAN_DELETE bit)
    //         (even though it's already off — practice the pattern)

    // Print final permissions
    printf("Permissions byte: 0x%02X\n", permissions);
    printf("Active: %s\n", (permissions & IS_ACTIVE) ? "yes" : "no");
    printf("Admin:  %s\n", (permissions & IS_ADMIN) ? "yes" : "no");
    printf("Read:   %s\n", (permissions & CAN_READ) ? "yes" : "no");
    printf("Write:  %s\n", (permissions & CAN_WRITE) ? "yes" : "no");
    printf("Delete: %s\n", (permissions & CAN_DELETE) ? "yes" : "no");

    return 0;
}
```

**Web dev analogy:** This is exactly how Unix file permissions work (`chmod 755`). Instead of `{ canRead: true, canWrite: true }` as separate booleans, you pack them into a single number.

---

## Exercise 5: Array + Pointer (bonus)

In JS: `arr[2]` gets the third element. In C, arrays and pointers are closely related.

```c
#include <stdio.h>

int main() {
    int readings[] = {23, 45, 67, 89, 12};
    int *ptr = readings;  // Points to first element

    // These two are the same:
    printf("Array syntax: %d\n", readings[2]);  // 67
    printf("Pointer math: %d\n", *(ptr + 2));   // 67

    // TODO: Print all 5 values using a for loop and pointer arithmetic
    // Hint: *(ptr + i) gives you element i

    return 0;
}
```

---

## Suggested Order

1. Exercise 1 (addresses) — 2 min
2. Exercise 2 (pointers) — 3 min
3. Exercise 3 (structs) — 5 min
4. Exercise 4 (bitwise flags) — 10 min ← this is the important one
5. Exercise 5 (arrays + pointers) — 5 min

Start with Exercise 1 and work through them. Let me know when you're done or stuck!

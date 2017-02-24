
Summation Example:

// C++ Code:

    int arr[32];
    int sum = 0;

    for (int i = 0; i < 32; i++) {
      sum += arr[i];
    }

// Note: &arr = &arr[0] = Memory Location 30

// Registers:
// r0 (rAcc)
// r1 - r15

// Some Example Instructions:
// li  - load immediate       - R[r0] = immediate
// lb  - load byte            - R[r0] = Mem[R[rs]]
// mov - move (copy)          - R[rs] = R[r0]
// add - addition             - R[rs] = R[rs] + R[rt]
// br  - branch               - PC = PC + R[r0]; a signed addition so you can
// bez - branch equal 0       - if (R[ov] == 0) then PC = PC + R[r0]
// bnez - branch not equal 0  - if (R[ov] != 0) then PC = PC + R[r0]
// slt - set less than        - R[ov] = if (R[rs] < R[rt]) ? 1:0
// inc - increment            - R[rs] += 1

// r1 = loop counter; initially 0
// r2 = initially 30 - Base memory location of arr[], arr[] goes from Mem[30] to Mem[70]
// r3 = sum; initially 0

// NOTE:  Your assembly code will NOT have labels like "loop" or "endloop". You
//        need a way of properly doing relative, absolute, or some custom method
//        of addressing what instruction to be run next. Meaning you will need to
//        spec

// Assembly Code: (using instructions I made for purposes of this example)

loop:
  li 32           // r0 = 32 ( i < 32)
  slt r1, r0      // if (r1 < r0) then R[ov] = 1
  li 7            // load 7 into r0 becuase "endloop" is 7 instructions forward
  bnez            // branch to endloop if R[ov] != 0; "endloop" is 6 instructions forward
  lb r2           // r0 = Mem[r2] = Mem[30]
  add r3, r0      // sum += r0
  inc r2          // increment address to get next byte in memory
  inc r1          // i++; increment loop counter i
  li -9           // load -9 into r0 because "loop" is 9 instructions backward
  br loop         // branch back to "loop" label; "loop" is 9 instructions backwards

endloop:

  // probably would want some instruction(s) here to store sum, which is in R[r3], to some location
  // in memory

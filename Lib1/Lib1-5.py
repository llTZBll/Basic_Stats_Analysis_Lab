def solve_equation():
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(10):
                xyz = 100 * x + 10 * y + z
                yzz = 100 * y + 10 * z + z
                if xyz + yzz == 532:
                    print(f"X={x}, Y={y}, Z={z}")

solve_equation()
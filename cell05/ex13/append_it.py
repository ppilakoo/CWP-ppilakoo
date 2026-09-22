#!/usr/bin/env python3

import sys

# ถ้าไม่มี parameter ส่งมาเลย
if len(sys.argv) == 1:
    print("none")
else:
    for param in sys.argv[1:]:
        # ถ้าไม่ได้ลงท้ายด้วย "ism" ให้เติม "ism" แล้วพิมพ์
        if not param.endswith("ism"):
            print(f"{param}ism")
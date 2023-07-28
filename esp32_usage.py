import gc
import os
from ili9341 import color565
from mySetup import display, unispace
import time

def df():
  s = os.statvfs('//')
  return ((s[0]*s[3])/1048576)

def free(full=False):
  F = gc.mem_free()
  A = gc.mem_alloc()
  T = F+A
  P = '{0:.2f}%'.format(F/T*100)
  result = [T, F, P]
  return result

def print_usage():
    flash = df()
    memory = free()
    line = 0
    print("{} MB".format(flash))
    print("Total: {} Free: {} [{}]".format(memory[0], memory[1], memory[2]))
    
    try:
        display.clear()
        display.draw_text(0, line, 'Disk: {} MB'.format(flash), unispace, color565(255, 128, 0))
        line += 24
        time.sleep(1)
        display.draw_text(0, line, 'Memory:', unispace, color565(255, 128, 0))
        line += 24
        display.draw_text(0, line, "Total: {}".format(memory[0]), unispace, color565(255, 128, 0))
        line += 24
        time.sleep(1)
        display.draw_text(0, line, "Free: {} [{}%]".format(memory[1], memory[2]), unispace, color565(255, 128, 0))
        time.sleep(5)
    except Exception as e:
        print ("No LCD found")

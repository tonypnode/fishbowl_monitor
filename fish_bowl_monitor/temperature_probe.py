import os
import glob


class TempData:
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

    def read_temp(self):
        with open(self.device_file, 'r') as f:
            lines = [x for x in f.readlines()]
            equals_pos = lines[1].find('t=')
            if equals_pos != -1:
                temp_string = lines[1][equals_pos + 2:]
                temp_c = float(temp_string) / 1000.0
                temp_f = temp_c * 9.0 / 5.0 + 32.0
                output = "%.1f" % temp_f
                return output

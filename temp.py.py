import os
import glob
import time
 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


class Temp_sensor():
    
    def __init__(self):
        pass
        
    def read_temp_raw(self):
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines
        
    def read_temp(self):
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find('t=')
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f   
            
    def print_current_room_temperature(self):
        while True:
            my_sensor = Temp_sensor()
            temperatur_celsius = my_sensor.read_temp()
            print(f'Temperature: {temperatur_celsius:.2f} °C')
            time.sleep(1)


def main():
    DS18B20 = Temp_sensor()
    DS18B20.print_current_room_temperature()
    
    
if __name__ == '__main__':
    main()



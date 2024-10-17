import os
import platform
import psutil
import json
import subprocess
import time
import ifcfg
    
# 
start_time_program = time.time()
    
# Получаем имя сисетмы , архитектру, версию сис-мы, имя пк в сети
def sys_info_one():
    name_system = platform.uname()
    name_system_2 = platform.node()
    name_system_3 = platform.platform()
    
    encoding = ['utf-8']
    pack = {
        "имя системы":name_system,
        "имя в сети":name_system_2,
        "архитектура":name_system_3,
    }
    for line in pack:
        if ':' in line:
            key, value = line.split(':', 1)
            pack[key.strip()] = value.strip()
    with open('my_file.json', 'w', encoding='utf-8') as f:
        json.dump(pack, f , indent = 4, ensure_ascii=False)
sys_info_one()

# ifconfig
def network_info():
    """
    Gets network information using `ifcfg` and returns it as a JSON string.
    """
    network_info = {}
    for interface in ifcfg.interfaces():
        network_info[interface] = ifcfg.interfaces()[interface]
    #return json.dumps(network_info)
    with open('ifconf.json', 'w') as f:
        json.dump(network_info, f, indent=4)

network_info()


# dns (nslookup)
def nslookup_to_json():
    """
    Выполняет команду nslookup и сохраняет результат в файл в формате JSON.
    """
    hostname = input("Введите имя хоста: ")
    filename = input("Введите имя файла: ")
    process = subprocess.run(['nslookup', hostname], capture_output=True, text=True)
    output = process.stdout
    result = {}
    for line in output.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip()
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4)

nslookup_to_json()

# dns (dig)

def dig_to_json():
    """
    Выполняет команду dig и сохраняет результат в файл в формате JSON.
    """
    hostname = input("Введите имя хоста: ")
    filename = input("Введите имя файла: ")
    process = subprocess.run(['dig', hostname], capture_output=True, text=True)
    output = process.stdout
    result = {}
    for line in output.splitlines():
        if ':' in line:
            key, value = line.split(':', 1)
            result[key.strip()] = value.strip()
    with open(filename, 'w') as f:
        json.dump(result, f, indent=4)
        
dig_to_json()


zeta = {}
for i,j,f in os.walk(r"/home/sla/"):
    #print(i)
    for js in i:
        #print(js)
        zeta[js] = os.path.join(i,js)
    for fs in f:
        #print(fs)
        zeta[js] = os.path.join(i,fs)
    
    with open("sysinfo.json", "w") as file:
        json.dump((zeta), file, indent=4, ensure_ascii=False)

# Работаем с процессами
def run_top_and_capture_output(duration=15):
    """Runs the 'top' command and captures its output for a specified duration.
    Args:
        duration: The duration in seconds to run 'top'.
    Returns:
        A list of lines from the 'top' output.
    """
    process = subprocess.Popen(['top', '-b', '-n', '1'], stdout=subprocess.PIPE)
    output = []
    start_time = time.time()
    while time.time() - start_time < duration:
        line = process.stdout.readline().decode('utf-8').strip()
        output.append(line)
    process.kill()
    return output
if __name__ == "__main__":
    top_output = run_top_and_capture_output()
    
    # Convert output to JSON format
    top_output_json = {
        "top_output": top_output
    }
    with open("top_output.json", "w") as f:
        json.dump(top_output_json, f, indent=4)   

run_top_and_capture_output()

# Читаем и записываем логи

def write_logs_to_json():
    """Collects system logs using various journalctl commands and writes them to a JSON file."""
    logs = {}
    logs['kernel_logs'] = subprocess.check_output(['sudo', 'journalctl', '-ek']).decode('utf-8')
    logs['error_logs'] = subprocess.check_output(['sudo', 'journalctl', '-p', '0']).decode('utf-8')
    logs['warning_logs'] = subprocess.check_output(['sudo', 'journalctl', '-p', '1']).decode('utf-8')
    logs['info_logs'] = subprocess.check_output(['sudo', 'journalctl', '-p', '2']).decode('utf-8')
    with open('system_logs.json', 'w') as f:
        json.dump(logs, f, indent=4)
write_logs_to_json()

# Получаем информацию о месте на диске

def get_memory_info():
    """Returns information about system memory usage."""
    memory = psutil.virtual_memory()
    return {
        'total': memory.total,
        'available': memory.available,
        'percent': memory.percent,
        'used': memory.used,
        'free': memory.free
    }
if __name__ == '__main__':
    memory_data = get_memory_info()
    # Combine data into a dictionary
    system_info = {
        'memory': memory_data,
    }
    # Save data to a JSON file
    with open('memory.json', 'w') as f:
        json.dump(system_info, f, indent=4)

get_memory_info()


def get_hardware_info():
    """Returns information about hardware, including buses and RAM."""
    # Use 'lshw' or 'dmidecode' for more detailed hardware info
    # Example using 'lshw'
    output = subprocess.check_output(['sudo','lshw', '-C', 'processor']).decode('utf-8') 
    output_1 = subprocess.check_output(['sudo','lshw', '-C', 'memory']).decode('utf-8') 
    output_2 = subprocess.check_output(['sudo','lshw', '-C', 'cpuid']).decode('utf-8') 
    output_3 = subprocess.check_output(['sudo','lshw', '-C', 'usb']).decode('utf-8') 
    output_4 = subprocess.check_output(['sudo','lshw', '-C', 'network']).decode('utf-8') 
    
    
    #return output,output_1,output_2,output_3,output_4
    # Combine data into a dictionary
    return {
    f'processor': output,
        f'memory': output_1,
        f'cpuid': output_2,
        f'usb': output_3,
        f'network': output_4,
    }

if __name__ == '__main__':
    memory_data = get_hardware_info()

    # Save data to a JSON file
    with open('system_info_2.json', 'w') as f:
        json.dump(memory_data, f, indent=4)

get_hardware_info()


def get_network_info():
    """Returns information about open network protocols."""
    connections = []
    for conn in psutil.net_connections():
        connections.append({
            'laddr': conn.laddr,
            'raddr': conn.raddr,
            'status': conn.status,
            'type': conn.type,
            'pid': conn.pid
        })
    return connections

# Example of using the functions:
if __name__ == '__main__':
    network_data = get_network_info()

    # Combine data into a dictionary
    system_info = {
        'network': network_data
    }

    # Save data to a JSON file
    with open('connection_info.json', 'w') as f:
        json.dump(system_info, f, indent=4)

get_network_info()


end_time_program = time.time()
print(f"Время затраченное на выаолнение программы в сек: {end_time_program - start_time_program}")


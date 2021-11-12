Get-NetIPAddress -AddressFamily IPv4 |Out-File -FilePath D:\IP.txt
curl ifconfig.me |Add-Content -Path D:\IP.txt 


nmap -sP 192.168.100.2/24 |Add-Content -Path D:\IP.txt
nmap --script=http-auth-finder instagram.com |Add-Content -Path D:\IP.txt
nmap -sP instagram.com |Add-Content -Path D:\IP.txt

$ip64 = Get-Content -Path D:\IP.txt 
$bytes = [System.Text.Encoding]::Unicode.GetBytes($ip64)
$enodedtext = [Convert]::ToBase64String($bytes)
$enodedtext |Out-File -FilePath D:\IP.txt
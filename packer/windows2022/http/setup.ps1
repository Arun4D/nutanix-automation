# Enable WinRM and necessary firewall rules to let Packer connect
netsh advfirewall firewall set rule group="Windows Remote Management" new enable=yes
cmd.exe /c winrm quickconfig -q
cmd.exe /c winrm set "winrm/config" '@{MaxTimeoutms="1800000"}'
cmd.exe /c winrm set "winrm/config/winrs" '@{MaxMemoryPerShellMB="1024"}'
cmd.exe /c winrm set "winrm/config/service" '@{AllowUnencrypted="true"}'
cmd.exe /c winrm set "winrm/config/client" '@{AllowUnencrypted="true"}'
cmd.exe /c winrm set "winrm/config/service/auth" '@{Basic="true"}'
cmd.exe /c winrm set "winrm/config/client/auth" '@{Basic="true"}'

# Stop WinRM Service just to reset the configurations effectively
Stop-Service winrm -Force
netsh firewall add portopening TCP 5985 "Port 5985"
Start-Service winrm

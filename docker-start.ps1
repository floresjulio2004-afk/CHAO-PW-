$ip = (Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object {
        $_.InterfaceAlias -like "*Wi-Fi*" -and
        $_.IPAddress -notlike "169.254.*"
    } |
    Select-Object -First 1 -ExpandProperty IPAddress)

Write-Host ""
Write-Host "==================================================" 
Write-Host " C.H.A.O. ha iniciado :)"
Write-Host "=================================================="
Write-Host ""
Write-Host " Acceso desde este ordenandor:"
Write-Host " http://localhost"
Write-Host ""
Write-Host " Acceso desde otros dispositivos:"
Write-Host " http://$ip"
Write-Host ""
Write-Host "=================================================="
Write-Host ""

docker compose up
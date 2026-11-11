$ip = (Get-NetIPAddress -AddressFamily IPv4 |
    Where-Object {
        $_.InterfaceAlias -like "*Wi-Fi*" -and
        $_.IPAddress -notlike "169.254.*" -and
        $_.IPAddress -ne "127.0.0.1"
    } |
    Select-Object -First 1 -ExpandProperty IPAddress)


Write-Host ""
Write-Host "=================================================="
Write-Host " C.H.A.O. ha iniciado :)"
Write-Host "=================================================="
Write-Host ""
Write-Host " Acceso desde este ordenador:"
Write-Host " http://localhost"
Write-Host ""
if ($ip) {
    Write-Host " Acceso desde otros dispositivos:"
    Write-Host " http://$ip"
} else {
    Write-Host " No se encontró una dirección IPv4 Wi-Fi."
}
Write-Host ""
Write-Host "=================================================="
Write-Host ""
docker compose up --build
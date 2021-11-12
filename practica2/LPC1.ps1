
function Operacion (){
    if ($opc -eq 1){
        $res = ($param1 * 4)
        Write-Host $res
    }

    if ($opc -eq 2){
        $res = ($param1 * $param1)
        Write-Host $res
    }

    if ($opc -eq 3){
        $res = ($param1 * 2) + ($param2 * 2)
        Write-Host $res 
    }
    
    if ($opc -eq 4){
        $res = ($param1 * $param2)
        Write-Host $res
    }

    if ($opc -eq 5){
        $res = $param1 + $param2 + $param3
        Write-Host $res
    }

    if ($opc -eq 6){
        $res = ($param1 * $param2)/2
        Write-Host $res
    }
    
}

while ($true){
    Write-Host "Que desas hacer?"
    $opc = Read-Host "
    1.Perimetro del Cuadrado
    2.Area del Cuadrado
    3.Permietro del Rectangulo
    4.Area del Rectangulo
    5.Perimetro del Triangulo
    6.Area del Triangulo
    7.Salir
    "
    
    if ($opc -eq 1) {
        [int]$param1 = Read-Host "Escribe el valor del lado del Cuadrado "
        Operacion ($opc, $param1)
    } 

    if ($opc -eq 2){
        [int]$param1 = Read-Host "Escribe el valor del lado del Cuadrado"
        Operacion ($opc, $param1)
    }

    if ($opc -eq 3){
        [int]$param1 = Read-Host "Largo del Rectangulo"
        [int]$param2 = Read-Host "Ancho del Rectangulo"
        Operacion ($opc, $param1, $param2)

    }

    if ($opc -eq 4){
        [int]$param1 = Read-Host "Largo del Rectangulo"
        [int]$param2 = Read-Host "Ancho del Rectangulo"
        Operacion ($opc, $param1, $param2)
    }

    if ($opc -eq 5){
        [int]$param1 = Read-Host "Lado1 del Triangulo"
        [int]$param2 = Read-Host "Lado2 del Traingulo"
        [int]$param3 = Read-Host "Lado3 del Triangulo"
        Operacion ($opc, $param1, $param2, $param2)
    }

    if ($opc -eq 6){
        [int]$param1 = Read-Host "Base del Triangulo"
        [int]$param2 = Read-Host "Altura del Triangulo"
        Operacion ($opc, $param1, $param2)
    }

    if ($opc -eq 7){
        Write-Host "Adios"
        break
    }

    else{
        Write-Host "Prueba de nuevo"
    }

} 
from AutoCode.AutoCode import AutoCode

autoCode = AutoCode()

usuario = [
'id_usuario','nombre', 'apellido', 'celular', 'direccion'
]
autoCode.generate("usuarios", usuario)

vehiculo = [
    'id_vehiculo','matricula', 'estado', 'usuario_id'
]
autoCode.generate("vehiculos", vehiculo)

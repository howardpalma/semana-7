"""
Módulo que define la clase Recurso, que representa un recurso del sistema
(puede ser un archivo, conexión, dispositivo, etc.)
"""

class Recurso:
    """
    Clase que representa un recurso del sistema.
    
    El constructor (__init__) inicializa el recurso con un estado específico.
    El destructor (__del__) se encarga de liberar el recurso de forma segura.
    """
    
    def __init__(self, id_recurso: str, tipo: str = "archivo", modo: str = "lectura"):
        """
        Constructor de la clase Recurso.
        
        Inicializa:
        1. Identificador único del recurso
        2. Tipo de recurso (archivo, conexión, dispositivo, etc.)
        3. Modo de acceso (lectura, escritura, lectura/escritura)
        4. Estado del recurso (abierto/cerrado)
        5. Marca temporal de creación
        
        Parámetros:
        id_recurso: identificador único del recurso
        tipo: tipo de recurso (por defecto "archivo")
        modo: modo de acceso (por defecto "lectura")
        """
        self.id_recurso = id_recurso
        self.tipo = tipo
        self.modo = modo
        self.estado = "abierto"
        self.fecha_creacion = "2024-01-01"  # En una implementación real sería datetime.now()
        self.contenido = f"Contenido inicial del recurso {id_recurso}"
        
        print(f"[CONSTRUCTOR] Recurso '{id_recurso}' creado (tipo: {tipo}, modo: {modo})")
    
    def leer(self) -> str:
        """Método para leer el contenido del recurso."""
        if self.estado == "cerrado":
            raise ValueError("No se puede leer un recurso cerrado")
        return self.contenido
    
    def escribir(self, contenido: str):
        """Método para escribir en el recurso."""
        if self.estado == "cerrado":
            raise ValueError("No se puede escribir en un recurso cerrado")
        if self.modo == "lectura":
            raise ValueError("Recurso abierto solo en modo lectura")
        self.contenido = contenido
        print(f"Contenido del recurso '{self.id_recurso}' actualizado")
    
    def cerrar(self):
        """Método para cerrar explícitamente el recurso."""
        if self.estado == "abierto":
            self.estado = "cerrado"
            print(f"Recurso '{self.id_recurso}' cerrado explícitamente")
    
    def __del__(self):
        """
        Destructor de la clase Recurso.
        
        Se ejecuta automáticamente cuando:
        1. El objeto sale del ámbito (scope)
        2. Se llama a 'del objeto' explícitamente
        3. El recolector de basura de Python elimina el objeto
        
        Realiza:
        1. Verificación del estado del recurso
        2. Cierre seguro si está abierto
        3. Registro de la liberación
        4. Notificación (simulada) al sistema
        
        Nota: En Python, el momento exacto de ejecución del destructor
        no está garantizado debido al recolector de basura.
        """
        try:
            if hasattr(self, 'estado') and self.estado == "abierto":
                print(f"[DESTRUCTOR] Advertencia: Recurso '{self.id_recurso}' aún estaba abierto")
                print(f"[DESTRUCTOR] Cerrando recurso '{self.id_recurso}' de forma segura...")
                # Simular limpieza de recursos del sistema
                # En un caso real: cerrar archivos, liberar memoria, etc.
                self.estado = "liberado"
                print(f"[DESTRUCTOR] Recurso '{self.id_recurso}' liberado correctamente")
            elif hasattr(self, 'estado'):
                print(f"[DESTRUCTOR] Recurso '{self.id_recurso}' ya estaba cerrado")
        except Exception as e:
            print(f"[DESTRUCTOR] Error al liberar recurso '{self.id_recurso}': {e}")
    
    def __str__(self):
        """Representación en string del recurso."""
        return f"Recurso(id={self.id_recurso}, tipo={self.tipo}, estado={self.estado})"
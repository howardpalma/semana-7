"""
Punto de entrada principal del programa.

Demuestra el uso de constructores y destructores en diferentes escenarios.
"""

from modelos.recurso import Recurso
from modelos.usuario import Usuario
from servicios.gestor_recursos import GestorRecursos
from servicios.gestor_usuarios import GestorUsuarios

def demostrar_constructores():
    """Demuestra el uso de constructores."""
    print("=" * 60)
    print("DEMOSTRACIÓN DE CONSTRUCTORES")
    print("=" * 60)
    
    # 1. Creación de objetos con constructor
    print("\n1. Creando recursos con diferentes parámetros:")
    recurso1 = Recurso("doc1", "documento", "lectura")
    recurso2 = Recurso("log1", "archivo_log", "escritura")
    
    print("\n2. Creando usuarios con valores por defecto y personalizados:")
    usuario1 = Usuario("U001", "Ana García", "ana@email.com")
    usuario2 = Usuario("U002", "Luis Martínez")  # Email por defecto
    
    return recurso1, recurso2, usuario1, usuario2

def demostrar_destructores_automaticos():
    """Demuestra la llamada automática a destructores."""
    print("\n" + "=" * 60)
    print("DESTRUCTORES AUTOMÁTICOS (al salir del ámbito)")
    print("=" * 60)
    
    # Los destructores se llamarán automáticamente al salir de esta función
    print("\nCreando objetos locales en una función...")
    recurso_local = Recurso("temp1", "temporal")
    usuario_local = Usuario("U999", "Temporal")
    
    print("\nSaliendo de la función... los destructores se llamarán automáticamente")
    # Al terminar la función, recurso_local y usuario_local salen del ámbito
    # y sus destructores deberían ejecutarse

def demostrar_destructores_explicitos():
    """Demuestra la llamada explícita a destructores con 'del'."""
    print("\n" + "=" * 60)
    print("DESTRUCTORES EXPLÍCITOS (usando 'del')")
    print("=" * 60)
    
    recurso_explicito = Recurso("exp1", "explicito")
    print("\nEliminando objeto explícitamente con 'del'...")
    del recurso_explicito  # Llama al destructor inmediatamente
    print("Objeto eliminado explícitamente")

def demostrar_gestor_recursos():
    """Demuestra el uso del gestor de recursos."""
    print("\n" + "=" * 60)
    print("GESTIÓN DE RECURSOS CON SERVICIO")
    print("=" * 60)
    
    gestor = GestorRecursos(capacidad_maxima=3)
    
    # Crear recursos a través del gestor
    r1 = gestor.crear_recurso("gestor1", "configuracion")
    r2 = gestor.crear_recurso("gestor2", "datos")
    
    # Usar los recursos
    print(f"\nContenido de gestor1: {r1.leer()[:30]}...")
    
    # El destructor del gestor se llamará al salir de esta función
    # y cerrará todos los recursos automáticamente

def demostrar_ciclo_vida_completo():
    """Demuestra un ciclo de vida completo de objetos."""
    print("\n" + "=" * 60)
    print("CICLO DE VIDA COMPLETO")
    print("=" * 60)
    
    # Crear gestor de usuarios
    gestor_usuarios = GestorUsuarios()
    
    # Registrar usuarios
    usuario1 = gestor_usuarios.registrar_usuario("A001", "Carlos Ruiz", "carlos@empresa.com")
    usuario2 = gestor_usuarios.registrar_usuario("A002", "María López")
    
    # Crear recursos
    recurso_importante = Recurso("informe_final", "documento")
    
    # Asignar recurso a usuario
    usuario1.asignar_recurso(recurso_importante)
    
    # Mostrar estado
    print("\nEstado actual del sistema:")
    gestor_usuarios.mostrar_usuarios()
    print(f"Recurso creado: {recurso_importante}")
    
    # Eliminar usuario (llamará a destructor si no hay otras referencias)
    print("\nEliminando usuario del gestor...")
    gestor_usuarios.eliminar_usuario("A001")
    
    # Forzar recolección de basura para ver destructores
    import gc
    print("\nForzando recolección de basura...")
    gc.collect()

def demostrar_excepciones_destructor():
    """Demuestra el manejo de excepciones en destructores."""
    print("\n" + "=" * 60)
    print("MANEJO DE EXCEPCIONES EN DESTRUCTORES")
    print("=" * 60)
    
    class RecursoCritico:
        def __init__(self, nombre):
            self.nombre = nombre
            self.abierto = True
            print(f"Recurso crítico '{nombre}' creado")
        
        def __del__(self):
            try:
                if self.abierto:
                    # Simular un error durante la liberación
                    print(f"Intentando liberar recurso '{self.nombre}'...")
                    raise RuntimeError("Error simulado en la liberación")
            except Exception as e:
                print(f"[DESTRUCTOR] Error manejado: {e}")
                # Intentar liberación alternativa
                print("[DESTRUCTOR] Ejecutando limpieza de emergencia...")
            finally:
                print(f"[DESTRUCTOR] Finalizado procesamiento para '{self.nombre}'")
    
    rc = RecursoCritico("critico1")
    print("Eliminando recurso crítico...")
    del rc

def main():
    """Función principal del programa."""
    print("PROGRAMA DE DEMOSTRACIÓN: CONSTRUCTORES Y DESTRUCTORES")
    print("=" * 60)
    
    try:
        # Demostración 1: Constructores
        objetos = demostrar_constructores()
        
        # Demostración 2: Destructores automáticos
        demostrar_destructores_automaticos()
        
        # Demostración 3: Destructores explícitos
        demostrar_destructores_explicitos()
        
        # Demostración 4: Gestor de recursos
        demostrar_gestor_recursos()
        
        # Demostración 5: Ciclo de vida completo
        demostrar_ciclo_vida_completo()
        
        # Demostración 6: Excepciones en destructores
        demostrar_excepciones_destructor()
        
        # Mantener referencias para evitar destrucción prematura
        print("\n" + "=" * 60)
        print("REFERENCIAS MANTENIDAS DESDE main()")
        print("=" * 60)
        print(f"Objetos creados en main: {len(objetos)}")
        print("Estos objetos se destruirán al final del programa")
        
    except Exception as e:
        print(f"\nError durante la ejecución: {e}")
    
    print("\n" + "=" * 60)
    print("FIN DEL PROGRAMA - LOS DESTRUCTORES FINALES SE EJECUTARÁN AHORA")
    print("=" * 60)

if __name__ == "__main__":
    main()
    
    # Forzar recolección final para ver todos los destructores
    import gc
    print("\nRecolección final de basura...")
    gc.collect()
    print("Programa terminado.")
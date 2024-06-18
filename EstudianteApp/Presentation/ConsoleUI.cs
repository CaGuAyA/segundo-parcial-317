using System;  // Agrega esta línea para incluir el espacio de nombres System
using EstudianteApp.Business;
using EstudianteApp.Data;

namespace EstudianteApp.Presentation
{
    public class ConsoleUI
    {
        private EstudianteService _estudianteService;

        public ConsoleUI()
        {
            _estudianteService = new EstudianteService();
        }

        public void MostrarMenu()
        {
            Console.WriteLine("Ingrese el ID del estudiante:");
            int id;
            while (!int.TryParse(Console.ReadLine(), out id))
            {
                Console.WriteLine("Por favor, ingrese un número válido.");
            }

            var estudiante = _estudianteService.ObtenerEstudiantePorId(id);

            if (estudiante != null)
            {
                MostrarEstudiante(estudiante);
            }
            else
            {
                Console.WriteLine("Estudiante no encontrado.");
            }
        }

        private void MostrarEstudiante(Estudiante estudiante)
        {
            Console.WriteLine($"ID: {estudiante.Id}");
            Console.WriteLine($"Nombre: {estudiante.Nombre}");
            Console.WriteLine($"Edad: {estudiante.Edad}");
            Console.WriteLine($"Carrera: {estudiante.Carrera}");
        }
    }
}

using System.Collections.Generic;
using System.Linq;

namespace EstudianteApp.Data
{
    public class EstudianteRepository
    {
        private List<Estudiante> estudiantes = new List<Estudiante>
        {
            new Estudiante { Id = 1, Nombre = "Juan Pérez", Edad = 20, Carrera = "Ingeniería" },
            new Estudiante { Id = 2, Nombre = "María López", Edad = 22, Carrera = "Medicina" },
            // Agrega más estudiantes si es necesario
        };

        public Estudiante ObtenerEstudiantePorId(int id)
        {
            return estudiantes.FirstOrDefault(e => e.Id == id);
        }
    }
}

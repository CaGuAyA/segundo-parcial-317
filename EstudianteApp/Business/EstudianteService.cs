using EstudianteApp.Data;

namespace EstudianteApp.Business
{
    public class EstudianteService
    {
        private EstudianteRepository _repository;

        public EstudianteService()
        {
            _repository = new EstudianteRepository();
        }

        public Estudiante ObtenerEstudiantePorId(int id)
        {
            return _repository.ObtenerEstudiantePorId(id);
        }
    }
}

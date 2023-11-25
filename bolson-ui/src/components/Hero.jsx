import img_hero from "../index_img.jpg";

export const Hero = () => {
  const jumbotronStyle = {
    position: 'relative',
    background: `url('${img_hero}') center/cover no-repeat`,
    color: 'white',
    height: '600px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  };

  const containerStyle = {
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
  };

  return (
    <div className="jumbotron jumbotron-fluid mb-5" style={jumbotronStyle}>
      <div className="container text-center col-lg-6 my-5" style={containerStyle}>
        <div className="my-4">
          <h2 className="display-4">AUDIENCIA PÚBLICA 2023</h2>
          <h4 className="display-4">Proyecto de Sistema de Desagües Cloacales</h4>

          <p className="lead">
            La Municipalidad de El Bolsón informa que, mediante la resolución municipal 409/2023, se convoca a una audiencia pública en el marco del procedimiento de Evaluación del Estudio de Impacto Ambiental del proyecto de "Sistema de Desagües Cloacales para la Ciudad de El Bolsón”.
          </p>
        </div>

        <a
          className="btn btn-success btn-lg rounded-pill mb-4"
          href="http://elbolson2025.pythonanywhere.com/prensa/nota/audiencia-publica-2023-proyecto-de-sistema-de-desagues-cloacales/"
          role="button"
          style={{ color: 'white' }}
        >
          Más Información
        </a>
      </div>
    </div>
  );
};




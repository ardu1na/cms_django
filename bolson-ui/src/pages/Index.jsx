import React from 'react';
import { Link } from 'react-router-dom';

const IndexPage = ({ articles }) => {
  return (
    <div>
      <div className="jumbotron jumbotron-fluid mb-5" style={{ position: 'relative', background: `url('./path/to/index_img.jpg') center/cover no-repeat`, color: 'white', height: '600px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <div className="container text-center col-lg-6 my-5" style={{ backgroundColor: 'rgba(0, 0, 0, 0.5)', padding: '-50px', marginTop: '150px' }}>
          <div className="my-4">
            <h2 className="display-4">AUDIENCIA PÚBLICA 2023</h2>
            <h4 className="display-4">Proyecto de Sistema de Desagües Cloacales</h4>

            <p className="lead">
              La Municipalidad de El Bolsón informa que, mediante la resolución municipal 409/2023, se convoca a una audiencia pública en el marco del procedimiento de Evaluación del Estudio de Impacto Ambiental del proyecto de "Sistema de Desagües Cloacales para la Ciudad de El Bolsón”.
            </p>
          </div>

          <a className="btn btn-success btn-lg rounded-pill mb-4" href="http://elbolson2025.pythonanywhere.com/prensa/nota/audiencia-publica-2023-proyecto-de-sistema-de-desagues-cloacales/" role="button" style={{ color: 'white' }}>Más Información</a>
        </div>
      </div>

      <br />

      {articles && (
        <div className="container mt-5">
          <h2 className="my-4">Últimas noticias</h2>

          <div className="row mb-5">
            {articles.map((article) => (
              <div className="col-md-4 mb-4" key={article.id}>
                <div className="card" style={{ height: '100%' }}>
                  <img
                    src={article.image_top ? article.image_top.url : (article.image_bottom ? article.image_bottom.url : './path/to/logo.png')}
                    className="card-img-top"
                    alt={`${article.titulo} Municipalidad de El Bolsón`}
                  />

                  <div className="card-body">
                    <h5 className="card-title"><Link to={article.get_absolute_url}>{article.titulo}</Link></h5>
                    <p className="text-extra-small mt-3"><i className="bi bi-calendar-week pe-2"></i> Publicado el {article.fecha}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default IndexPage;

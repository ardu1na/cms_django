import React from 'react';

const Footer = () => {
  return (
    <footer className="justify-content-around mx-0 bg-dark d-flex p-4">
      <div className="row pt-3">

        <div className="col mt-4 d-none d-sm-block">
          <img src={require('./path/to/logo_escudo.png')} alt="Logo Municipalidad El Bolsón" width="120" />
        </div>

        <div className="col text-white my-4 mx-5">
          <h5><span>TELÉFONOS DE EMERGENCIA</span></h5>
          <ul className="nav flex-column">
            <li className="nav-item mb-2 text-secondary"><strong>911</strong> | Emergencias</li>
            <li className="nav-item mb-2 text-secondary"><strong>100</strong> | Bomberos</li>
            <li className="nav-item mb-2 text-secondary"><strong>103</strong> | Incendios forestales</li>
            <li className="nav-item mb-2 text-secondary"><strong>107</strong> | Hospital</li>
            <li className="nav-item mb-2 text-secondary"><strong>135</strong> | Gendarmería Nacional</li>
          </ul>
        </div>

        <div className="col text-white my-5 mx-5">
          <h5>SEGUINOS EN LAS REDES</h5>
          <a href="https://www.facebook.com/MunicipalidadElBolson" className="text-secondary fs-4 px-3" title="Facebook" aria-label="Facebook"><i className="bi bi-facebook"></i></a>
          <a href="https://www.instagram.com/municipalidadelbolson/" className="text-secondary fs-4 px-3" title="Instagram" aria-label="Instagram"><i className="bi bi-instagram"></i></a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;

import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="navbar navbar-expand-lg navbar-light bg-light">
      <div className="container">
        <Link className="navbar-brand" to="/index">
          <img src={require('./path/to/logo.png')} alt="Logo" height="85" />
        </Link>

        <button className="navbar-toggler mx-4" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation" style={{ borderWidth: 0 }}>
          <span className="navbar-toggler-icon"></span>
        </button>

        <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <Link className="nav-link" to="/index">Inicio </Link>
            </li>

            <li className="nav-item dropdown">
              <a className="nav-link dropdown-toggle" href="#" id="serviciosDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                Servicios
              </a>
              <div className="dropdown-menu" aria-labelledby="serviciosDropdown">
                <Link className="dropdown-item" to="/consultar-deuda">Consultar deuda</Link>
              </div>
            </li>

            <li className="nav-item">
              <Link className="nav-link" to="/prensa">Prensa</Link>
            </li>
          </ul>
        </div>
      </div>
    </header>
  );
};

export default Header;

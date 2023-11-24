import { Link } from "react-router-dom";
import logo from "../logo.png";


export const Header = () => {
  return (
    <>
      <header className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container">
            <img className="navbar-brand" src={logo} alt="Logo" height="85" />         

            <div className="collapse navbar-collapse justify-content-end" id="navbarNav">
                <ul className="navbar-nav">
                    <li className="nav-item active">
                        <Link className="nav-link"  to="/">Inicio</Link>
                    </li>                  
                
                    <li className="nav-item">
                        <Link className="nav-link" to="/blogs">Prensa</Link>

                    </li>
                </ul>
            </div>
        </div>
    </header>
  

    </>
  )
};


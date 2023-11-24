import './boton.css';

export function Boton({ onClick, label }) {
   
    return (
       
        <button
          className = 'btn-dark'
          onClick = {onClick}>
          {label}
        </button>
        
    )
  }
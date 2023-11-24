import React from 'react';
import Header from './Header'; 
import Footer from './Footer';

const BaseLayout = ({ children }) => {
  return (
    <div className="container-fluid m-0 p-0">
      <Header />

      <div>
        hola
        {children}
      </div>

      <Footer />
    </div>
  );
};

export default BaseLayout;

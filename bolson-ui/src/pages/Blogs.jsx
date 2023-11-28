import React, { useEffect, useState } from 'react';
import { SideBar } from "../components/SideBar";
import { Destacados } from "../components/Destacados";

export function Blogs() {
  const [articulos, setArticulos] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);

  const fetchData = async (page) => {
    try {
      const response = await fetch(`http://localhost:8000/api/prensa/articulos/?page=${page}`);
      const data = await response.json();
      setArticulos(data.results);
      setTotalPages(data.total_pages);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
    fetchData(currentPage);
  }, [currentPage]);

  return (
    <>
      <div className="container my-4">
        <div className="row py-5">
          <div className="col-md-8 mb-4">
            {articulos.length > 0 ? (
              <div className="row">
                {articulos.map((article) => (
                  <div className="col-md-6 mb-4" key={article.id}>
                    <div className="card" style={{ height: '100%' }}>
                    <img
                      src={article.image_top ? article.image_top : article.image_bottom ? article.image_bottom : '/static/img/logo.png'}
                      alt={`${article.titulo} Municipalidad de El Bolsón`}
                      className="card-img-top"
                    />

                      <div className="card-body">
                        <h5 className="card-title">
                          <a href={article.get_absolute_url}>{article.titulo}</a>
                        </h5>
                        <br />
                        <p className="text-extra-small">
                          <i className="bi bi-calendar-week pe-2"></i> Publicado el {article.fecha}
                        </p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="card border-0">
                <div className="card-body">
                  <p className="card-text text-secondary">No se han encontrado artículos, prueba con otra palabra.</p>
                </div>
              </div>
            )}

            {/* Pagination Controls */}
            <div className="d-flex justify-content-center mt-4">
              <button
                className="btn btn-outline-primary mx-2"
                disabled={currentPage === 1}
                onClick={() => setCurrentPage(currentPage - 1)}
              >
                Previous
              </button>
              <span>{`Page ${currentPage} of ${totalPages}`}</span>
              <button
                className="btn btn-outline-primary mx-2"
                disabled={currentPage === totalPages}
                onClick={() => setCurrentPage(currentPage + 1)}
              >
                Next
              </button>
            </div>
          </div>

          <SideBar />
        </div>

        <Destacados />
      </div>
    </>
  );
}

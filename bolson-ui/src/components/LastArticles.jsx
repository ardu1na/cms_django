import React, { useState, useEffect } from 'react';
import logo from "../logo.png";

export const LastArticles = () => {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/prensa/last/');
        const data = await response.json();
        setArticles(data);
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles();
  }, []);

  return (
    <div className="container mt-5">
      <h2 className="my-4">Últimas noticias</h2>

      <div className="row mb-5">
        {articles.map((article) => (
          <div key={article.id} className="col-md-4 mb-4">
            <div className="card" style={{ height: '100%' }}>
              <img
              src={`http://127.0.0.1:8000/${article.image_top}`}
              className="card-img-top"
                alt={`${article.titulo} Municipalidad de El Bolsón`}
              />

              <div className="card-body">
                <h5 className="card-title">
                  <a>{article.titulo}</a>
                </h5>
                <p className="text-extra-small mt-3">
                  <i className="bi bi-calendar-week pe-2"></i> Publicado el {article.fecha}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};


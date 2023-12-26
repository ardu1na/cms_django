import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

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

  if (articles.length === 0) {
    return null;
  }

  return (
    <div className="container mt-5">
      <Link className="text-decoration-none text-secondary mt-5" to="/prensa"><h2>Últimas noticias</h2></Link>

      <div className="row my-5">
        {articles.map((article) => (
          <div key={article.id} className="col-md-4 mb-4">
            <div className="card" style={{ height: '100%' }}>
              <img
             src={article.image_top ? article.image_top : article.image_bottom ? article.image_bottom : '/static/img/logo.png'}
              className="card-img-top"
                alt={`${article.titulo} Municipalidad de El Bolsón`}
              />

              <div className="card-body">
                <h5 className="card-title">
                <Link to={`/prensa/${article.id}`}>
                   <a>{article.titulo}</a> 
                    </Link>
                </h5>
                <p className="text-extra-small mt-3">
                  <i className="bi bi-calendar-week pe-2"></i> Publicado el {article.date}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};


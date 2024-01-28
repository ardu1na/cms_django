import React, { useState, useEffect } from 'react';
import { Link } from "react-router-dom";

export const SideBar = () => {
  const [ultimas, setUltimas] = useState([]);
  const [tags, setTags] = useState([]);

  // Fetch data from your Django API endpoints
  useEffect(() => {
    const fetchUltimas = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/prensa/last/list/');
        const data = await response.json();
        setUltimas(data);
      } catch (error) {
        console.error('Error fetching ultimas:', error);
      }
    };

    const fetchTags = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/prensa/tags/list/');
        const data = await response.json();
        setTags(data);
      } catch (error) {
        console.error('Error fetching tags:', error);
      }
    };

    fetchUltimas();
    fetchTags();
  }, []);

  return (
    <div className="col-md-3 ms-4">
      {ultimas.length > 0 && (
        <>
          <h5>ÚLTIMAS NOTICIAS</h5>
          <hr />
          {ultimas.map((article) => (
            <div className="row" key={article.id}>
              <div className="col-2 pe-0 pe-3 d-flex flex-row-reverse">
                <i className="bi bi-file-earmark-text-fill"></i>
              </div>
              <div className="col-10 ps-0 me-0">

              <Link
                className="text-decoration-none text-secondary"
                to={`/prensa/${article.id}`}
                replace
              >
                {article.titulo}
              </Link>

                  
              </div>
            </div>
          ))}
        </>
      )}

      {tags.length > 0 && (
        <div className="row my-5">
          <h5>TAGS</h5>
          <hr />
          {tags.map((tag) => (
            <a
              key={tag.id}
              className="text-decoration-none mx-1"
            >
              <span className="badge rounded-pill text-bg-success">
                {tag.nombre}
              </span>
            </a>
          ))}
        </div>
      )}
    </div>
  );
};


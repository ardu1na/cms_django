import React, { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import  { SideBar } from "../components/SideBar";

export function BlogDetail() {
  const { blogId } = useParams();
  const [blogData, setBlogData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/prensa/articulos/${blogId}`);
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }

        const data = await response.json();
        setBlogData(data);
      } catch (error) {
        console.error("Error fetching blog data:", error);
      }
    };

    fetchData();
  }, [blogId]);

  if (!blogData) {
    return <p>Loading...</p>;
  }

  return (
    <>
    <div className="container my-4">
      
      <nav aria-label="breadcrumb">
        <ol className="breadcrumb my-5">
          <li className="breadcrumb-item"><Link className="text-decoration-none text-secondary" to="/"><i className="bi bi-house-door-fill"></i> <strong>Inicio</strong></Link></li>
          <li className="breadcrumb-item"><Link className="text-decoration-none text-secondary" to="/prensa"><strong>Prensa</strong></Link></li>
          <li className="breadcrumb-item active" aria-current="page">{blogData.titulo}</li>
        </ol>
      </nav>

      <div className="row">
        <div className="col-md-8 mb-4">
          <div className="card">
            <div className="card-body">

              <h3 className="card-title pt-3 text-secondary">{blogData.titulo}</h3>

              <br />
              <p className="text-extra-small"><i className="bi bi-calendar-week pe-2"></i> Publicado el {blogData.date}</p>
              <p className="card-text">
                {blogData.tags.map((tag) => (
                  <Link to={`/tag/${tag.slug}`} key={tag.id}><span className="badge rounded-pill text-bg-success">{tag.nombre}</span></Link>
                ))}
              </p>
              <hr />

              {blogData.image_top && <img src={blogData.image_top} className="img-fluid mt-1 mb-3" alt={`${blogData.titulo} - Prensa de la Municipalidad de El Bolsón`} />}

              <p className="card-text" dangerouslySetInnerHTML={{ __html: blogData.texto }} />

              {blogData.image_bottom && <img src={blogData.image_bottom} className="img-fluid my-2" alt={`${blogData.titulo} - Prensa de la Municipalidad de El Bolsón`} />}

            </div>
            {blogData.updated && (
              <>
                <hr />
                <p className="text-secondary mx-3"> (actualizado: {blogData.updated})</p>
              </>
            )}
          </div>
        </div>

        <SideBar />
      </div>
    </div>
    </>
  );
}

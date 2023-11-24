import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

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
    <div>
      <h2>{blogData.titulo}</h2>
      <p>Blog ID: {blogData.id}</p>
      <div dangerouslySetInnerHTML={{ __html: blogData.texto }} />
    </div>
  );
}

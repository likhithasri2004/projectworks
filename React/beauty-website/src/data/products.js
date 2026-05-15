import { useEffect, useState } from "react";

const Products = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("https://dummyjson.com/products/category/skincare?limit=15")
      .then((res) => res.json())
      .then((data) => {
        console.log("API DATA:", data);
        setProducts(data.products);
      })
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h2>Beauty Products</h2>

      {products.length === 0 && <p>Loading...</p>}

      {products.map((item) => (
        <div key={item.id}>
          <h4>{item.title}</h4>
          <img src={item.thumbnail} width="150" />
          <p>₹ {item.price}</p>
        </div>
      ))}
    </div>
  );
};

export default Products;
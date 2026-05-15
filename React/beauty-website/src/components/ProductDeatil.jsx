import React, { useState, useEffect, useContext } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { CartContext } from '../App.jsx';

const ProductDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { addToCart } = useContext(CartContext);

  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // ✅ SAFE VITE IMAGE PATHS
  const fallbackImages = Array.from(
    { length: 20 },
    (_, i) => `${import.meta.env.BASE_URL}images/img${i + 1}.png`
  );

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        setLoading(true);
        setError(null);

        const res = await fetch(
          'https://makeup-api.herokuapp.com/api/v1/products.json'
        );
        const data = await res.json();

        const found = data.find(
          item => String(item.id) === String(id)
        );

        if (!found) throw new Error('Product not found');

        setProduct(found);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  if (error || !product) {
    return (
      <div className="not-found">
        <h2>Product Not Found</h2>
        <button onClick={() => navigate('/products')}>Back</button>
      </div>
    );
  }

  // ✅ ALWAYS SAME IMAGE FOR SAME PRODUCT
  const fallbackImage =
    fallbackImages[Number(product.id) % fallbackImages.length];

  return (
    <section className="product-detail-page">
      <div className="container">
        <button onClick={() => navigate('/products')}>
          ← Back
        </button>

        <div className="product-detail-grid">
          <img
            src={product.image_link || fallbackImage}
            alt={product.name}
            onError={(e) => {
              e.currentTarget.src = fallbackImage;
            }}
            style={{ width: '300px' }}
          />

          <div>
            <h1>{product.name}</h1>
            <p>${product.price || 'N/A'}</p>

            <button onClick={() => addToCart(product)}>
              Add to Cart
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductDetail;
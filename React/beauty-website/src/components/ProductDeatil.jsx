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

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        setLoading(true);
        setError(null);

        // ✅ FETCH ALL PRODUCTS (API LIMITATION)
        const response = await fetch(
          'https://makeup-api.herokuapp.com/api/v1/products.json'
        );
        const data = await response.json();

        const foundProduct = data.find(
          item => String(item.id) === String(id)
        );

        if (!foundProduct) {
          throw new Error('Product not found');
        }

        setProduct(foundProduct);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProduct();
  }, [id]);

  const handleAddToCart = () => {
    addToCart(product);
  };

  /* ---------- LOADING ---------- */
  if (loading) {
    return (
      <section className="product-detail-page">
        <div className="container">
          <div className="loading">Loading product details... ✨</div>
        </div>
      </section>
    );
  }

  /* ---------- ERROR ---------- */
  if (error || !product) {
    return (
      <section className="product-detail-page">
        <div className="container">
          <div className="not-found">
            <h2>Product Not Found 😢</h2>
            <button
              className="btn btn-primary"
              onClick={() => navigate('/products')}
            >
              Browse Products
            </button>
          </div>
        </div>
      </section>
    );
  }

  /* ---------- UI ---------- */
  return (
    <section className="product-detail-page">
      <div className="container">
        <button className="back-button" onClick={() => navigate('/products')}>
          ← Back to Products
        </button>

        <div className="product-detail-grid">
          <div className="product-images">
            <img
              src={
                product.image_link ||
                'https://via.placeholder.com/500x600?text=No+Image'
              }
              alt={product.name}
              className="main-image"
            />
          </div>

          <div className="product-info">
            <h1 className="product-title">{product.name}</h1>

            <div className="product-price-large">
              ${product.price || 'N/A'}
            </div>

            <div className="product-badges">
              {product.brand && (
                <span className="brand-badge">{product.brand}</span>
              )}
              {product.product_type && (
                <span className="type-badge">{product.product_type}</span>
              )}
            </div>

            {product.description && (
              <div className="product-description">
                <h3>About this product</h3>
                <p>{product.description}</p>
              </div>
            )}

            <button
              className="add-to-cart-btn large"
              onClick={handleAddToCart}
            >
              🛒 Add to Cart
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default ProductDetail;
import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const ProductCarousel = () => {
  const [featuredProducts, setFeaturedProducts] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch('https://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline')
      .then(res => res.json())
      .then(data => {
        setFeaturedProducts(data.slice(0, 10));
        setLoading(false);
      })
      .catch(err => {
        console.error('Carousel fetch error:', err);
        setLoading(false);
      });
  }, []);

  useEffect(() => {
    if (featuredProducts.length > 0) {
      const interval = setInterval(() => {
        setCurrentIndex((prev) => (prev + 1) % featuredProducts.length);
      }, 4000);
      return () => clearInterval(interval);
    }
  }, [featuredProducts.length]);

  const nextSlide = () => setCurrentIndex((prev) => (prev + 1) % featuredProducts.length);
  const prevSlide = () => setCurrentIndex((prev) => (prev - 1 + featuredProducts.length) % featuredProducts.length);

  if (loading) {
    return (
      <section className="carousel-section">
        <div className="container">
          <div className="loading-carousel">Loading featured products... ✨</div>
        </div>
      </section>
    );
  }

  if (featuredProducts.length === 0) {
    return (
      <section className="carousel-section">
        <div className="container">
          <div className="empty-carousel">No featured products available</div>
        </div>
      </section>
    );
  }

  return (
    <section className="carousel-section">
      <div className="container">
        <h2 className="section-title">✨ Featured Products</h2>
        <div className="carousel-container">
          <button className="carousel-arrow left" onClick={prevSlide} aria-label="Previous slide">
            ‹
          </button>
          
          <div 
            className="carousel-track" 
            style={{ transform: `translateX(-${currentIndex * 100}%)` }}
          >
            {featuredProducts.map((product) => (
              <div key={product.id} className="carousel-slide">
                <Link to={`/products/${product.id}`} className="product-card carousel-card">
                  <div className="product-image">
                    <img 
                      src={product.image_link || 'https://via.placeholder.com/400x500/f9d5e5/9c4a7c?text=No+Image'}
                      alt={product.name}
                      loading="lazy"
                    />
                  </div>
                  <div className="product-info">
                    <h3>{product.name}</h3>
                    <div className="product-meta">
                      <span className="brand">{product.brand}</span>
                      <span className="price">${product.price || 'N/A'}</span>
                    </div>
                  </div>
                </Link>
              </div>
            ))}
          </div>
          
          <button className="carousel-arrow right" onClick={nextSlide} aria-label="Next slide">
            ›
          </button>
        </div>
        <div className="carousel-cta">
          <Link to="/products" className="btn btn-primary">View All Products</Link>
        </div>
      </div>
    </section>
  );
};

export default ProductCarousel;
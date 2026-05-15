import React from 'react';
import ProductCarousel from '../components/ProductCarousel';

const Home = () => {
  return (
    <>
      <section className="hero">
        <div className="hero-content">
          <h1>Discover Your Perfect Glow ✨</h1>
          <p>Premium makeup from world-class brands. Authentic products, fast shipping, unbeatable prices.</p>
          <div className="hero-buttons">
            <a href="/products" className="btn btn-primary btn-large">Shop Now</a>
            <a href="/products" className="btn btn-outline btn-large">Browse Collection</a>
          </div>
        </div>
      </section>

      <ProductCarousel />

      <section className="features-section">
        <div className="container">
          <div className="features-grid">
            <div className="feature">
              <div className="feature-icon">🚚</div>
              <h3>Free Shipping</h3>
              <p>Orders over $50 ship free</p>
            </div>
            <div className="feature">
              <div className="feature-icon">✅</div>
              <h3>100% Authentic</h3>
              <p>Guaranteed genuine products</p>
            </div>
            <div className="feature">
              <div className="feature-icon">↩️</div>
              <h3>30-Day Returns</h3>
              <p>Hassle-free returns</p>
            </div>
          </div>
        </div>
      </section>
    </>
  );
};

export default Home;
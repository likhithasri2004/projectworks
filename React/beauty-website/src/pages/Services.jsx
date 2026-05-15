import React from "react";

const Services = () => {
  return (
    <section className="services-page">
      <div className="container">
        {/* Hero */}
        <div className="services-hero">
          <h1>Our Services</h1>
          <p>
            Beauty services designed to make your shopping experience smooth,
            safe, and delightful.
          </p>
        </div>

        {/* Intro */}
        <div className="services-section">
          <h2>✨ What We Do</h2>
          <p>
            At <strong>BeautyGlow</strong>, we go beyond selling beauty products.
            We focus on providing services that help you choose the right
            products, shop confidently, and enjoy a premium beauty experience
            from start to finish.
          </p>
        </div>

        {/* Services Grid */}
        <div className="services-grid">
          <div className="service-card">
            <h3>💄 Beauty Product Curation</h3>
            <p>
              We carefully curate skincare and makeup products from trusted
              brands to ensure quality, safety, and effectiveness for all skin
              types.
            </p>
          </div>

          <div className="service-card">
            <h3>🧴 Personalized Recommendations</h3>
            <p>
              Find products that match your skin type, tone, and preferences
              with our thoughtfully organized categories and filters.
            </p>
          </div>

          <div className="service-card">
            <h3>🛒 Easy & Secure Shopping</h3>
            <p>
              Enjoy a smooth shopping journey with secure checkout, simple cart
              management, and a user-friendly interface.
            </p>
          </div>

          <div className="service-card">
            <h3>📦 Fast & Reliable Delivery</h3>
            <p>
              We ensure safe packaging and reliable delivery so your beauty
              essentials reach you in perfect condition.
            </p>
          </div>

          <div className="service-card">
            <h3>🔍 Detailed Product Information</h3>
            <p>
              Every product comes with clear descriptions, pricing, brand
              details, and images to help you make informed decisions.
            </p>
          </div>

          <div className="service-card">
            <h3>💬 Customer Support</h3>
            <p>
              Our friendly support team is always ready to assist you with
              product queries, orders, or general assistance.
            </p>
          </div>
        </div>

        {/* Why Section */}
        <div className="services-section highlight">
          <h2>💖 Why Our Services Matter</h2>
          <p>
            We believe beauty shopping should be stress-free and enjoyable. Our
            services are built to save your time, offer clarity, and deliver
            confidence with every purchase.
          </p>
        </div>

        {/* Footer Text */}
        <div className="services-footer">
          <h3>✨ Because You Deserve the Best</h3>
          <p>
            From discovery to delivery, BeautyGlow services are designed to give
            you a glowing experience every step of the way.
          </p>
        </div>
      </div>
    </section>
  );
};

export default Services;
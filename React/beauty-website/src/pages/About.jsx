import React from "react";

const About = () => {
  return (
    <section className="about-page">
      <div className="container">
        {/* Hero Section */}
        <div className="about-hero">
          <h1>About BeautyGlow</h1>
          <p>
            Enhancing natural beauty through confidence, care, and quality
            products.
          </p>
        </div>

        {/* Intro */}
        <div className="about-section">
          <h2>✨ Who We Are</h2>
          <p>
            <strong>BeautyGlow</strong> is an online beauty destination created
            for people who believe that beauty starts with self-care and
            confidence. We bring together a wide range of skincare and makeup
            products that are thoughtfully curated to suit every skin type,
            tone, and style.
          </p>
        </div>

        {/* Mission + Vision */}
        <div className="about-grid">
          <div className="about-card">
            <h3>🌿 Our Mission</h3>
            <p>
              Our mission is to make beauty accessible, inclusive, and enjoyable
              for everyone. We aim to provide high-quality beauty products with
              honest information, so you can shop with confidence.
            </p>
          </div>

          <div className="about-card">
            <h3>🌸 Our Vision</h3>
            <p>
              We envision a world where beauty is not defined by trends or
              standards, but by individuality and self-expression. BeautyGlow
              exists to celebrate uniqueness.
            </p>
          </div>
        </div>

        {/* What We Offer */}
        <div className="about-section">
          <h2>💄 What We Offer</h2>
          <ul className="about-list">
            <li>✔ Skincare products for all skin types</li>
            <li>✔ Makeup essentials for everyday & special occasions</li>
            <li>✔ Trusted and cruelty-free beauty brands</li>
            <li>✔ Affordable prices with premium quality</li>
            <li>✔ Smooth and secure shopping experience</li>
          </ul>
        </div>

        {/* Why Choose Us */}
        <div className="about-section highlight">
          <h2>💖 Why Choose BeautyGlow?</h2>
          <p>
            We are passionate about beauty and committed to quality. Every
            product on BeautyGlow is selected with care to ensure safety,
            performance, and satisfaction.
          </p>
          <p>
            From browsing to checkout, our goal is to give you a seamless and
            delightful shopping experience.
          </p>
        </div>

        {/* Closing */}
        <div className="about-footer">
          <h3>✨ Glow Confidently. Glow Beautifully.</h3>
          <p>
            Join the BeautyGlow community and discover products that help you
            feel confident, radiant, and empowered every day.
          </p>
        </div>
      </div>
    </section>
  );
};

export default About;
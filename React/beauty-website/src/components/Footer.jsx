import React from 'react';

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          <div className="footer-brand">
            <h3>✨ BeautyGlow</h3>
            <p>Your destination for premium beauty products from top brands worldwide.</p>
          </div>
          <div className="footer-links">
            <h4>Quick Links</h4>
            <ul>
              <li><a href="/">Home</a></li>
              <li><a href="/products">Products</a></li>
              <li><a href="/about">About</a></li>
              <li><a href="/contact">Contact</a></li>
            </ul>
          </div>
          <div className="footer-contact">
            <h4>Get in Touch</h4>
            <p>Email: hello@beautyglow.com</p>
            <p>Phone: (555) 123-4567</p>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; 2024 BeautyGlow. All rights reserved. | Made with ❤️ for beauty lovers</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
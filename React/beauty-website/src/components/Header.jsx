import React, { useState, useContext } from 'react';
import { Link, useLocation } from 'react-router-dom';
import { CartContext } from '../App.jsx';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const { cartItems } = useContext(CartContext);
  const location = useLocation();

  return (
    <header className="header">
      <div className="container">
        <Link to="/" className="logo" onClick={() => setIsMenuOpen(false)}>
          <h2>✨ BeautyGlow</h2>
        </Link>
        
        <nav className={`nav ${isMenuOpen ? 'nav-open' : ''}`}>
          <Link 
            to="/" 
            className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Home
          </Link>
          <Link 
            to="/about" 
            className={`nav-link ${location.pathname === '/about' ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            About
          </Link>
          <Link 
            to="/services" 
            className={`nav-link ${location.pathname === '/services' ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Services
          </Link>
          <Link 
            to="/products" 
            className={`nav-link ${location.pathname.startsWith('/products') ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Products
          </Link>
          <Link 
            to="/contact" 
            className={`nav-link ${location.pathname === '/contact' ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(false)}
          >
            Contact
          </Link>
          <Link to="/cart" className="cart-btn" onClick={() => setIsMenuOpen(false)}>
            🛒 Cart ({cartItems.length})
          </Link>
        </nav>

        <button 
          className="menu-toggle" 
          onClick={() => setIsMenuOpen(!isMenuOpen)}
          aria-label="Toggle menu"
        >
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </header>
  );
};

export default Header;
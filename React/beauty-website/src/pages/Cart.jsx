import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { CartContext } from '../App.jsx';

const Cart = () => {
  const { cartItems, updateQuantity, removeFromCart, getTotalPrice } = useContext(CartContext);

  if (cartItems.length === 0) {
    return (
      <section className="cart-page">
        <div className="container">
          <div className="empty-cart">
            <h2>Your cart is empty 🛒</h2>
            <p>Looks like you haven't added anything to your cart yet.</p>
            <Link to="/products" className="btn btn-primary">Start Shopping</Link>
          </div>
        </div>
      </section>
    );
  }

  return (
    <section className="cart-page">
      <div className="container">
        <h1>Shopping Cart ({cartItems.length})</h1>
        
        <div className="cart-content">
          <div className="cart-items">
            {cartItems.map(item => (
              <div key={item.id} className="cart-item">
                <img 
                  src={item.image_link || 'https://via.placeholder.com/100x120'}
                  alt={item.name}
                  className="cart-item-image"
                />
                <div className="cart-item-details">
                  <h3>{item.name}</h3>
                  <p className="brand">{item.brand}</p>
                  <div className="price">${parseFloat(item.price || 0).toFixed(2)}</div>
                </div>
                <div className="quantity-control">
                  <button 
                    onClick={() => updateQuantity(item.id, item.quantity - 1)}
                    className="qty-btn"
                  >
                    -
                  </button>
                  <span className="qty">{item.quantity}</span>
                  <button 
                    onClick={() => updateQuantity(item.id, item.quantity + 1)}
                    className="qty-btn"
                  >
                    +
                  </button>
                </div>
                <div className="item-total">
                  ${(parseFloat(item.price || 0) * item.quantity).toFixed(2)}
                </div>
                <button 
                  className="remove-btn"
                  onClick={() => removeFromCart(item.id)}
                >
                  ×
                </button>
              </div>
            ))}
          </div>

          <div className="cart-summary">
            <h3>Order Summary</h3>
            <div className="summary-row">
              <span>Subtotal ({cartItems.length} items):</span>
              <span>${getTotalPrice().toFixed(2)}</span>
            </div>
            <div className="summary-row shipping">
              <span>Shipping:</span>
              <span>Free</span>
            </div>
            <div className="summary-total">
              <span>Total:</span>
              <span>${getTotalPrice().toFixed(2)}</span>
            </div>
            <button className="checkout-btn">Proceed to Checkout</button>
            <Link to="/products" className="continue-shopping">Continue Shopping</Link>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Cart;
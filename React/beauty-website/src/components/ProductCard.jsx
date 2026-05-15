import React from 'react';
import { Link } from 'react-router-dom';

const fallbackImages = Array.from(
  { length: 20 },
  (_, i) => `/images/img${i + 1}.png`
);

const ProductCard = ({ product, index }) => {
  const fallbackImage = fallbackImages[index % fallbackImages.length];

  return (
    <Link to={`/products/${product.id}`} className="product-link">
      <div className="product-card">
        <div className="product-image">
          <img
            src={product.image_link || fallbackImage}
            alt={product.name}
            onError={(e) => {
              e.target.src = fallbackImage;
            }}
          />
        </div>

        <div className="product-info">
          <h3 className="product-name">{product.name}</h3>
          <p className="product-brand">{product.brand || 'Unknown Brand'}</p>

          <div className="product-footer">
            <span className="product-price">
              ${product.price || 'N/A'}
            </span>
            <button className="add-btn">View</button>
          </div>
        </div>
      </div>
    </Link>
  );
};

export default ProductCard;
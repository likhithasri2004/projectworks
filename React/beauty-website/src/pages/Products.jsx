import React, { useState, useEffect, useCallback } from 'react';
import { Link } from 'react-router-dom';
import ProductCard from '../components/ProductCard';

const Products = () => {
  const [products, setProducts] = useState([]);
  const [filteredProducts, setFilteredProducts] = useState([]);
  const [loading, setLoading] = useState(true);

  const [searchTerm, setSearchTerm] = useState('');
  const [selectedBrand, setSelectedBrand] = useState('');
  const [brands, setBrands] = useState([]);

  /* =========================
     FETCH PRODUCTS (ONLY 20)
  ========================== */
  const fetchProducts = useCallback(async () => {
    try {
      setLoading(true);

      const response = await fetch(
        'https://makeup-api.herokuapp.com/api/v1/products.json'
      );
      const data = await response.json();

      const limitedProducts = data.slice(0, 20); // ✅ ONLY 20

      setProducts(limitedProducts);
      setFilteredProducts(limitedProducts);

      const uniqueBrands = Array.from(
        new Set(limitedProducts.map(p => p.brand).filter(Boolean))
      );
      setBrands(uniqueBrands);
    } catch (error) {
      console.error('Error fetching products:', error);
    } finally {
      setLoading(false);
    }
  }, []);

  /* =========================
     RESET FILTERS ON PAGE LOAD
  ========================== */
  useEffect(() => {
    setSearchTerm('');
    setSelectedBrand('');
    fetchProducts();
  }, [fetchProducts]);

  /* =========================
     FILTER LOGIC
  ========================== */
  useEffect(() => {
    let filtered = [...products];

    if (searchTerm.trim()) {
      filtered = filtered.filter(product =>
        product.name?.toLowerCase().includes(searchTerm.toLowerCase()) ||
        product.brand?.toLowerCase().includes(searchTerm.toLowerCase())
      );
    }

    if (selectedBrand) {
      filtered = filtered.filter(
        product => product.brand === selectedBrand
      );
    }

    setFilteredProducts(filtered);
  }, [searchTerm, selectedBrand, products]);

  /* =========================
     LOADING STATE
  ========================== */
  if (loading) {
    return (
      <section className="products-page">
        <div className="container">
          <div className="loading">Loading beautiful products... ✨</div>
        </div>
      </section>
    );
  }

  /* =========================
     UI
  ========================== */
  return (
    <section className="products-page">
      <div className="container">
        {/* HEADER */}
        <div className="page-header">
          <div>
            <h1>All Products ({filteredProducts.length})</h1>
            <p className="subtitle">Showing 20 beauty products</p>
          </div>

          <input
            type="text"
            placeholder="🔍 Search products, brands..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="search-input"
          />
        </div>

        {/* FILTER */}
        {brands.length > 0 && (
          <div className="filters">
            <select
              value={selectedBrand}
              onChange={(e) => setSelectedBrand(e.target.value)}
              className="brand-select"
            >
              <option value="">All Brands</option>
              {brands.map(brand => (
                <option key={brand} value={brand}>
                  {brand}
                </option>
              ))}
            </select>
          </div>
        )}

        {/* PRODUCTS GRID */}
        <div className="products-grid">
          {filteredProducts.map((product, index)=> (
            <ProductCard key={product.id} product={product} index={index} />
          ))}
        </div>

        {/* EMPTY STATE */}
        {filteredProducts.length === 0 && (
          <div className="empty-state">
            <h3>No products found 😔</h3>
            <p>Try clearing filters</p>

            <button
              className="btn btn-primary"
              onClick={() => {
                setSearchTerm('');
                setSelectedBrand('');
                setFilteredProducts(products);
              }}
            >
              Browse All Products
            </button>
          </div>
        )}
      </div>
    </section>
  );
};

export default Products;
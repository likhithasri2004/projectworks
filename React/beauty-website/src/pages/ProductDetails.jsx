import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

export default function ProductDetails() {
  const { id } = useParams()
  const [product, setProduct] = useState(null)

  useEffect(() => {
    fetch(`https://dummyjson.com/products/${id}`)
      .then(res => res.json())
      .then(data => setProduct(data))
  }, [id])

  if (!product) return <h2>Loading...</h2>

  return (
    <div>
      <img src={product.thumbnail} alt={product.title} width="200" />
      <h2>{product.title}</h2>
      <p>{product.description}</p>
      <h3>₹ {product.price * 80}</h3>
      <p>Rating: ⭐ {product.rating}</p>
    </div>
  )
}
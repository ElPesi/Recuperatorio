import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

function App() {
  const [product, setProduct] = useState([])
  const [newData, setNewData] = useState([])

  useEffect(() =>{
    getData
  }, [])

  const getData = () => {
    axios.get('https://fakestoreapi.com/products')
    .then(response = setProduct(response.data))
    .then(console.log(response.data))
  }
  const agregarData = () => {
    axios.post('https://fakestoreapi.com/products', newData)
    .then()
  }

  return (
    <>
      <h1>Electronic</h1>
      <p>Ingrese cantidad de productos que quiera ver</p>
      <input></input>
      <button onClick={getData}>Obtener</button>
      <p>{product}</p>
    </>
  )
}

export default App
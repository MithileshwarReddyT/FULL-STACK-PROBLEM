import axios from 'axios';
import React, { useEffect, useState } from 'react';
import './App.css';

const App = () => {
  const [dishes, setDishes] = useState([]);

  useEffect(() => {
    fetchDishes();
  }, []);

  const fetchDishes = async () => {
    try {
      const response = await axios.get('http://127.0.0.1:5000/api/dishes');
      setDishes(response.data);
    } catch (error) {
      console.error('Error fetching dishes:', error);
    }
  };

  const togglePublish = async (dishId) => {
    try {
      await axios.post(`http://127.0.0.1:5000/api/dishes/${dishId}/toggle`);
      fetchDishes();
    } catch (error) {
      console.error('Error toggling publish status:', error);
    }
  };

  return (
    <div>
      <h1>Dish Dashboard</h1>
      <ul>
        {dishes.map(dish => (
          <li key={dish.dishId}>
            <img src={dish.imageUrl} alt={dish.dishName} width="100" />
            <p>{dish.dishName}</p>
            <button onClick={() => togglePublish(dish.dishId)}>
              {dish.isPublished ? 'Unpublish' : 'Publish'}
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;

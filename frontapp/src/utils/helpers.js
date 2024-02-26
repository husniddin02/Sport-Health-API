// src/utils/helpers.js

export async function fetchData(endpoint, method = 'GET', body = null) {
    const requestOptions = {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    };
  
    try {
      const response = await fetch(endpoint, requestOptions);
      if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Fetch Error:', error);
      throw error;
    }
  }
  
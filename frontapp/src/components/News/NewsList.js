import React, { useState, useEffect } from 'react';
import axios from 'axios';

const NewsList = () => {
    const [news, setNews] = useState([]);

    useEffect(() => {
        // Получение списка новостей с сервера
        const fetchNews = async () => {
            try {
                const response = await axios.get('/api/news');
                setNews(response.data);
            } catch (error) {
                console.error('Error fetching news:', error);
            }
        };

        fetchNews();
    }, []);

    return (
        <div>
            <h2>News</h2>
            <ul>
                {news.map(item => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>
        </div>
    );
};

export default NewsList;

import React, { useState } from 'react';
import axios from 'axios'; // Подключаем axios для выполнения запросов на сервер

const ChangePassword = () => {
    // Состояния для полей ввода пароля
    const [passwords, setPasswords] = useState({
        currentPassword: '',
        newPassword: '',
        confirmNewPassword: ''
    });

    // Обработчик изменений в полях ввода пароля
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setPasswords({ ...passwords, [name]: value });
    };

    // Обработчик отправки формы
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (passwords.newPassword !== passwords.confirmNewPassword) {
            alert('New password and confirm password do not match.');
            return;
        }
        try {
            const response = await axios.put('/api/user/change-password', passwords); // Отправляем PUT запрос на сервер для изменения пароля
            alert(response.data.message); // Выводим сообщение об успешном изменении пароля
            setPasswords({ // Сбрасываем значения полей ввода после успешного изменения пароля
                currentPassword: '',
                newPassword: '',
                confirmNewPassword: ''
            });
        } catch (error) {
            console.error('Error changing password:', error);
        }
    };

    // Рендеринг формы изменения пароля
    return (
        <div className="change-password">
            <h2>Change Password</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Current Password:
                    <input type="password" name="currentPassword" value={passwords.currentPassword} onChange={handleInputChange} />
                </label>
                <label>
                    New Password:
                    <input type="password" name="newPassword" value={passwords.newPassword} onChange={handleInputChange} />
                </label>
                <label>
                    Confirm New Password:
                    <input type="password" name="confirmNewPassword" value={passwords.confirmNewPassword} onChange={handleInputChange} />
                </label>
                <button type="submit">Change Password</button>
            </form>
        </div>
    );
};

export default ChangePassword;

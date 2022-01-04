-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Янв 04 2022 г., 17:56
-- Версия сервера: 8.0.24
-- Версия PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `employees`
--

-- --------------------------------------------------------

--
-- Структура таблицы `employee`
--

CREATE TABLE `employee` (
  `id` int NOT NULL,
  `name` varchar(15) COLLATE utf8mb4_german2_ci NOT NULL,
  `occupation` varchar(20) COLLATE utf8mb4_german2_ci NOT NULL,
  `hire_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `salary` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_german2_ci;

--
-- Дамп данных таблицы `employee`
--

INSERT INTO `employee` (`id`, `name`, `occupation`, `hire_date`, `salary`) VALUES
(1, 'John', 'Manager', '2022-01-04 14:48:51', '120000'),
(2, 'Amy', 'Assistent', '2022-01-04 14:48:51', '3000'),
(3, 'Taylor', 'DS', '2022-01-04 14:50:44', '24000'),
(4, 'Anna', 'DE', '2022-01-04 14:50:44', '20000'),
(5, 'Shon', 'Engineer', '2022-01-04 14:53:08', '12000'),
(6, 'Niki', 'DE', '2022-01-04 14:53:08', '20001');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

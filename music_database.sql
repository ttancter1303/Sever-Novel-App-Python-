-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th10 09, 2022 lúc 04:44 PM
-- Phiên bản máy phục vụ: 10.4.25-MariaDB
-- Phiên bản PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `music_database`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `music`
--

CREATE TABLE `music` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `data` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Đang đổ dữ liệu cho bảng `music`
--

INSERT INTO `music` (`id`, `title`, `data`) VALUES
(38, 'This way', 'static/musics/1667923388.083587215190thisway-cara-6607957.mp3'),
(39, 'Co gai vang', 'static/musics/1667923420.91577446913cogaivang-huyrtungviu-6617041.mp3'),
(40, 'Gywn song', 'static/musics/1667993627.745560296431gwynlordofcinder-motoisakuraba-5922657.mp3'),
(41, 'Royal RÂT', 'static/musics/1667993695.72444735895920. royal rat authority.mp3'),
(42, 'Royal RÂT', 'static/musics/1667993700.67103675567520. royal rat authority.mp3'),
(43, 'Academy of Rây Lucaria', 'static/musics/1667993755.05087146406112_academy of raya lucaria.mp3'),
(44, 'Cold play', 'static/musics/1667993883.815297652092vivalavidacoldplaycover-jfla-4774051.mp3'),
(45, '021', 'static/musics/1667993914.716248832969021-binz-6720876.mp3');

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `music`
--
ALTER TABLE `music`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `music`
--
ALTER TABLE `music`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

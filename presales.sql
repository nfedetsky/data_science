/* Таблица хранения данных gj пресейлe*/

/* Упрощенная таблица, куда вносим данные о самом потенциальном Заказчике, с которым работаем по пресейлу,
данные об аккаунте и пресейл менеджерах, описание деятельности потенциального Заказчика и данные о потерциальном бюджете проекта*/

CREATE TABLE presales(
id_presale INT PRIMARY KEY AUTO_INCREMENT,
name_client VARCHAR(25) NOT NULL,
life BOOLEAN DEFAULT 1,
client_region VARCHAR(25) NOT NULL,
client_industry TINYTEXT,
data_registration DATE NOT NULL,
contact_name VARCHAR(30) NOT NULL,
contact_tel VARCHAR(12) NOT NULL,
contact_email VARCHAR(20) NOT NULL,
ka_manager VARCHAR(30) NOT NULL,
presale_manager VARCHAR(30) NOT NULL,
about TEXT,
content BLOB,
budget FLOAT(10,2) NOT NULL
);
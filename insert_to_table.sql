insert into presales (name_client, life, client_region, client_industry, data_registration, contact_name, contact_tel, contact_email, ka_manager, presale_manager, about, budget)
values 
('АвтоВаз', default, 'Тольяти', 'Автомобильная промышленность', '2022.12.23', 'Быков Александр', '+79172234565', 'bykov@tolyatiavto.ru', 'Зобов Дмитрий', 'Федецкий Николай', 'Есть потребность в доработке кадровой системы в части модуля учета обратной связи', 1000000),
('Транснефть', default, 'Москва', 'Нефтедобыча', '2023.01.20', 'Алиев Нугзар', '+74957892343', 'n.aliev@tn.com', 'Баринов Никита', 'Федецкий Николай', 'Требуется разработка бот-платформы', 30000000),
('Федеральное казначейство', default, 'Москва', 'Государственное учреждение', '2021.05.25', 'Усманов Руслан', '+74952233456', 'usmanov@roskazna.ru', 'Зобов Дмитрий', 'Федецкий Николай', 'В рамках импортозамещения, требуется разработка процессной платформы',6000000);

select * from presales
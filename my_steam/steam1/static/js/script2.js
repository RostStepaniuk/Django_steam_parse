// Путь к CSV файлу
const csvFilePath = '/media/games_list.csv';

// Загрузить данные из CSV файла
fetch(csvFilePath)
  .then(response => response.text())
  .then(data => {
    // Разбить данные CSV на строки
    const lines = data.split('\n');

    // Пропустить первую строку, так как она содержит заголовки
    for (let i = 1; i < lines.length; i++) {
      const line = lines[i];
      // Разбить строку на поля
      const fields = line.split(',');

      // Получить название игры, цену и скидочную цену
      const title = fields[0];
      const price = fields[1];
      const discPrice = fields[2];

      // Вывести информацию о игре в консоль
      console.log(`Название игры: ${title}`);
      console.log(`Цена: ${price}`);
      console.log(`Скидочная цена: ${discPrice}`);
      console.log('---');
    }
  })
  .catch(error => {
    console.error('Произошла ошибка при загрузке CSV файла:', error);
  });




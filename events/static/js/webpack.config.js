const path = require('path');

module.exports = {
  entry: './src/main.js',
  output: {
    filename: 'bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath: '/static/dist/',
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Применять правила только к JS файлам
        exclude: /node_modules/, // Исключить папку node_modules
        use: {
          loader: 'babel-loader', // Использовать Babel для транспиляции JS
          options: {
            presets: ['@babel/preset-env'], // Настройки пресетов Babel
          },
        },
      },
      // Добавьте дополнительные правила при необходимости
    ],
  },
  // Рассмотрите возможность добавления плагинов, если они нужны вашему проекту
};

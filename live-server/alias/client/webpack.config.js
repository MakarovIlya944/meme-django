const path = require('path');

module.exports = {
  entry: './src/client.js',
  output: {
    path: path.resolve(__dirname, '../../../meme/alias/static/js'),
    filename: 'bundle.js'
  }
};
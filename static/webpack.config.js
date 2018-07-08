const webpack = require('webpack');
const config = {
    entry:  __dirname + '/js/index.jsx',
    output: {
        path: __dirname + '/dist',
        filename: 'bundle.js',
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css']
    },
    module: {
      rules: [
          {
              test: /\.jsx?/,
              exclude: /node_modules/,
              use: 'babel-loader'
          },
          {
            test: /\.css$/,
            use: [
              "style-loader",
              {
                loader: "css-loader",
                options: {
                  modules: true, // default is false
                  sourceMap: true,
                  importLoaders: 1,
                  localIdentName: "[name]--[local]--[hash:base64:8]"
                }
              },
              "postcss-loader"
            ]
          },
      ]}
};
module.exports = config;
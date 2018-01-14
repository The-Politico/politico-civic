const gulp = require('gulp');
const webpack = require('webpack');
const webpackStream = require('webpack-stream');
const prodConfig = require('../../webpack-prod.config.js');


module.exports = () =>
  gulp.src('src/js/main.js')
    .pipe(webpackStream(prodConfig, webpack))
    .pipe(gulp.dest('./../static/'))
    .on('end', () => {
      process.exit();
    });

var gulp = require('gulp');
var sass = require('gulp-sass');

module.exports = () => gulp.src('./src/scss/**/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./../static/skins/css'));

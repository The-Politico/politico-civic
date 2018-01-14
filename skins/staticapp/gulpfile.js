const gulp = require('./gulp')([
  'dev',
  'build',
  'scss',
]);

gulp.task('watch', function () {
  gulp.watch('./src/scss/**/*.scss', ['scss']);
});

gulp.task('default', ['dev', 'watch']);

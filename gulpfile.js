import gulp from 'gulp';
import plumber from 'gulp-plumber';
import sass from 'gulp-dart-sass';
import postcss from 'gulp-postcss';
import autoprefixer from 'autoprefixer';
import csso from 'postcss-csso';
import rename from 'gulp-rename';
import htmlmin from 'gulp-htmlmin';
import terser from 'gulp-terser';
import squoosh from 'gulp-libsquoosh';
import svgo from 'gulp-svgmin';
import svgstore from 'gulp-svgstore';
import del from 'del';
import browser from 'browser-sync';
import {exec} from 'child_process';

// Styles

export const styles = () => {
  return gulp.src('source/sass/style.scss', {sourcemaps: true})

    .pipe(plumber())
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([
      autoprefixer(),
      csso()
    ]))
    .pipe(rename('style.min.css'))
    .pipe(gulp.dest('build/static/css', {sourcemaps: '.'}))
    .pipe(browser.stream());
}

// HTML

const html = () => {
  return gulp.src('source/*.html')
    .pipe(htmlmin({collapseWhitespace: true}))
    .pipe(gulp.dest('build/template'));
}

//Scripts

const scripts = () => {
  return gulp.src('source/js/*.js')
    .pipe(terser())
    .pipe(gulp.dest('build/static/js'));
}

//Images

const optimizeImages = () => {
  return gulp.src('source/img/**/*.{jpg,png}')
    .pipe(squoosh())
    .pipe(gulp.dest('build/static/img'));
}

const copyImages = () => {
  return gulp.src('source/img/**/*.{jpg,png}')
    .pipe(gulp.dest('build/static/img'));
}

//WebP

const createWebp = () => {
  return gulp.src(['source/img/**/*.{jpg,png}', '!source/img/favicons/*'])
    .pipe(squoosh({
      webp: {}
    }))
    .pipe(gulp.dest('build/static/img'));
}

//SVG

const svg = () =>
  gulp.src(['source/img/**/*.svg', '!source/img/sprite/*.svg'])
    .pipe(svgo())
    .pipe(gulp.dest('build/static/img'));

const sprite = () => {
  return gulp.src('source/img/sprite/*.svg')
    .pipe(svgo())
    .pipe(svgstore({
      inlineSvg: true
    }))
    .pipe(rename('sprite.svg'))
    .pipe(gulp.dest('build/static/img'));
}

//Copy

const copy = (done) => {
  gulp.src([
    'source/*.ico',
    'source/*.webmanifest',
    'source/js/*',
    'source/admin/**',
    'source/ckeditor/**'
  ], {
    base: 'source'
  })
    .pipe(gulp.dest('build/static'))
  done();
}

const copyFonts = (done) => {
  gulp.src([
    'source/fonts/*.{woff2,woff}',
  ], {
    base: 'source'
  })
    .pipe(gulp.dest('build/static'))
  done();
}

//Clean

const clean = () => {
  return del('build');
};

//Локальный запуск сервера через терминал
//-->

// export const startserver = (done) => {
//   exec('python manage.py runserver 8000');
//   done();
// }

// export const startservers = gulp.parallel(server, startserver);

//<--

//Server

export const server = (done) => {
  browser.init({
    baseDir: "./build",
    open: false,
    notify: true,
    port: 9090,
    proxy: '127.0.0.1:8000'
  })
  done();
}

//Reload

const reload = (done) => {
  browser.reload();
  done();
}

// Watcher

const watcher = () => {
  gulp.watch('source/sass/**/*.scss', gulp.series(styles));
  gulp.watch('source/js/*.js', gulp.series(scripts, reload));
  gulp.watch('source/*.html', gulp.series(html, reload));
}

//Build

export const build = gulp.series(
  clean,
  copy,
  copyFonts,
  optimizeImages,
  gulp.parallel(
    styles,
    html,
    scripts,
    svg,
    sprite,
    createWebp
  ),
);

//Default

export default gulp.series(
  clean,
  copy,
  copyFonts,
  copyImages,
  gulp.parallel(
    styles,
    html,
    scripts,
    svg,
    sprite,
    createWebp
  ),
  gulp.parallel(
    // startservers,
    server,
    watcher
  )
);

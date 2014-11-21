module.exports = (grunt) ->

  grunt.initConfig

    # Compile the SCSS file
    sass:
      dist:
        files:
          'grayscale/static/css/styles.css':
            'grayscale/static/css/styles.scss'

    # Autoprefix the resulting CSS file
    autoprefixer:
      css_file:
        src: 'grayscale/static/css/styles.css'
        dest: 'grayscale/static/css/styles.css'

    # Minify the CSS
    cssmin:
      dist:
        files: [
          expand: true
          cwd: 'grayscale/static/css',
          src: ['*.css', '!*.min.css'],
          dest: 'grayscale/static/css',
          ext: '.min.css'
        ]

    # Concatenate the JS files
    concat:
      options:
        separator: ';'
        sourceMap: true
      dist:
        src: [
          # Libraries
          'bower_components/jquery/dist/jquery.js',
          # Plugins
          'bower_components/dropzone/downloads/dropzone.js',
          # App scripts
          'grayscale/imageconvert/static/js/imageconvert.js'
        ]
        dest: 'grayscale/static/js/all.js'

    # Compress the concatenated JS file
    uglify:
      dist:
        files:
          'grayscale/static/js/all.min.js': 'grayscale/static/js/all.js'

    # Watch coffee and SASS files
    watch:
      scripts:
        files: ['grayscale/**/*.js']
        tasks: ['js']
        options:
          spawn: false
          livereload: true
      stylesheets:
        files: ['grayscale/**/*.scss']
        tasks: ['css']
        options:
          spawn: false
          livereload: true


  # Default task(s).
  grunt.registerTask 'default', ['css', 'js', 'watch']
  grunt.registerTask 'css', ['sass', 'autoprefixer', 'cssmin']
  grunt.registerTask 'js', ['concat', 'uglify']


  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-contrib-concat'
  grunt.loadNpmTasks 'grunt-contrib-uglify'
  grunt.loadNpmTasks 'grunt-contrib-cssmin'
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-sass'
  grunt.loadNpmTasks 'grunt-autoprefixer'

  return

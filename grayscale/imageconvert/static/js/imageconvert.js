Dropzone.options.myAwesomeDropzone = {
  paramName: "color_file",
  maxFilesize: 10,
  thumbnailWidth: null,
  thumbnailHeight: null,
  previewsContainer: '.images',
  previewTemplate: '<div class="row image-row"> \
      <div class="col-sm-6 color-image"> \
        <img data-dz-thumbnail width="100%" /> \
      </div> \
      <div class="col-sm-6 gray-image"> \
        <div class="spinner replace-me">\
          <div class="double-bounce1"></div> \
          <div class="double-bounce2"></div> \
        </div> \
      </div> \
    </div><hr/>',
  init: function() {
    this.on("success", function(file, response) {
      doPoll(response);
    });
  },
};

var doPoll = function(response) {
  url = '/tasks/status/' + response.task_id + '/';
  $.get(url, function(data) {

    if (data == "PENDING") {
      console.log("Still pending.");
      setTimeout(function() {
        doPoll(response)
      }, 200);
    }

    if (data == "SUCCESS") {
      url = '/tasks/result/' + response.task_id + '/';
      $.get(url, function(data) {
        img = $('<img/>').attr({
          'src': data,
          'width': '100%'
        });
        $('.replace-me:eq(0)').replaceWith(img);
      });
    }

  });
};
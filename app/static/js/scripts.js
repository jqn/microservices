// Javascript
$(document).ready(function () {
  $("#condition-select").change(function () {
    console.log("select changes", $("#condition-select").val());
    $("#year-select").empty();
    $("#make-select").empty();
    $("#model-select").empty();
    $.ajax({
      data: {
        condition: $("#condition-select").val(),
      },
      type: "POST",
      url: "api/v1.0/ratings/years",
      dataType: "JSON",
      success: function (data) {
        console.log("data res", data);
        for (i = 0; i < data.years.length; i++) {
          $("#year-select").append(
            '<option value="' +
              data.years[i] +
              '">' +
              data.years[i] +
              "</option>"
          );
        }
        $("#year-select").prepend(
          '<option value="default" selected>Select a year</option>'
        );
        $("#make-select").prepend(
          '<option value="default" selected>Select a make</option>'
        );
        $("#model-select").prepend(
          '<option value="default" selected>Select a model</option>'
        );
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#year-select").change(function () {
    console.log("select changes");
    $("#make-select").empty();
    $("#model-select").empty();
    $.ajax({
      data: {
        condition: $("#condition-select").val(),
        year: $("#year-select").val(),
      },
      type: "POST",
      url: "api/v1.0/ratings/makes",
      dataType: "JSON",
      success: function (data) {
        console.log("data res", data);
        for (i = 0; i < data.makes.length; i++) {
          $("#make-select").append(
            '<option value="' +
              data.makes[i] +
              '">' +
              data.makes[i] +
              "</option>"
          );
        }
        $("#make-select").prepend(
          '<option value="default" selected>Select a make</option>'
        );
        $("#model-select").prepend(
          '<option value="default" selected>Select a model</option>'
        );
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#make-select").change(function () {
    console.log("select changes");
    $("#model-select").empty();
    $.ajax({
      data: {
        condition: $("#condition-select").val(),
        year: $("#year-select").val(),
        make: $("#make-select").val(),
      },
      type: "POST",
      url: "api/v1.0/ratings/models",
      dataType: "JSON",
      success: function (data) {
        console.log("data res", data);
        $("#model-select").empty();
        for (i = 0; i < data.models.length; i++) {
          $("#model-select").append(
            '<option value="' +
              data.models[i] +
              '">' +
              data.models[i] +
              "</option>"
          );
        }
        $("#model-select").prepend(
          '<option value="default" selected>Select a model</option>'
        );
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#deal-ratings-form").on("submit", function (event) {
    event.preventDefault();
    $.ajax({
      data: {
        condition: $("#condition-select").val(),
        year: $("#year-select").val(),
        make: $("#make-select").val(),
        model: $("#model-select").val(),
      },
      type: "POST",
      url: "/api/v1.0/ratings",
      dataType: "JSON",
      complete: function () {
        // hide the preloader (progress bar)
        // $('#form-response').html("");
      },
      success: function (data) {
        var result = JSON.parse(data);
        console.log(result.great_price);
        // Display the returned data in browser
        var title = `${$("#condition-select").val()} ${$(
          "#year-select"
        ).val()} ${$("#make-select").val()} ${$("#model-select").val()}`;

        $("#results-title").text(title);
        $("#incredible-count").text(result.incredible.length);
        $("#great-count").text(result.great_price.length);
        $("#good-count").text(result.good_price.length);
        $("#fair-count").text(result.fair_price.length);
        $("#unknown-count").text(result.unknown.length);
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    }).done(function (data) {});
  });
});

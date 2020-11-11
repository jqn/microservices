// Javascript
$(document).ready(function () {
  $("#condition-select").change(function () {
    console.log("select changes", $("#condition-select").val());
    if ($("#condition-select").val() === "default") {
      $("#deal-ratings-form").trigger("reset");
      return;
    }
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
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#year-select").change(function () {
    console.log("select changes");
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
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#make-select").change(function () {
    console.log("select changes");
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
        for (i = 0; i < data.models.length; i++) {
          $("#model-select").append(
            '<option value="' +
              data.models[i] +
              '">' +
              data.models[i] +
              "</option>"
          );
        }
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#deal-ratings-form").on("submit", function (event) {
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
        if (result.incredible && result.incredible.length !== 0) {
          $("#incredible").html(result.incredible);
        }
        if (result.great_price && result.great_price.length !== 0) {
          $("#great").html(result.great_price[0].make);
        }
        if (result.good_price && result.good_price.length !== 0) {
          $("#good").html(result.good_price);
        }
        if (result.fair_price && result.fair_price.length !== 0) {
          $("#fair").html(result.fair_price);
        }
        if (result.unknown && result.unknown.length !== 0) {
          $("#fair").html(result.unknown);
        }
      },
      error: function (xhr) {
        console.log("error. see details below.");
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    }).done(function (data) {
      // console.log("data", JSON.parse(data))
      // $('#output').text(data.output).show();
    });
    event.preventDefault();
  });
});

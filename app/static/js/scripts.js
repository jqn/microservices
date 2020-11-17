// Javascript
$(document).ready(function () {
  localStorage.clear();

  $("#reset-button").click(function () {
    localStorage.clear();
    $("#deal-ratings-form").trigger("reset");
    $("#incredible-count").text(0);
    $("#great-count").text(0);
    $("#good-count").text(0);
    $("#fair-count").text(0);
    $("#unknown-count").text(0);
  });

  $("#condition-select").change(function () {
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
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#year-select").change(function () {
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
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    });
  });

  $("#make-select").change(function () {
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
        localStorage.setItem("resultsJSON", data);

        console.log(result);
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
        console.log(xhr.status + ": " + xhr.responseJSON);
      },
    }).done(function (data) {});
  });

  $("#incredible-count").click(function () {
    // Retrieving data:
    results = localStorage.getItem("resultsJSON");
    resultsObj = JSON.parse(results);
    if (resultsObj.incredible.length !== 0) {
      $(".results-table").empty();
      for (i = 0; i < resultsObj.incredible.length; i++) {
        $(".results-table").append(
          `<tr>
            <td>${resultsObj.incredible[i].year}</td>
            <td>${resultsObj.incredible[i].make}</td>
            <td>${resultsObj.incredible[i].model}</td>
            <td>${resultsObj.incredible[i].series}</td>
            <td>${resultsObj.incredible[i].mileage}</td>
          </tr>`
        );
      }
    }
  });

  $("#great-count").click(function () {
    // Retrieving data:
    results = localStorage.getItem("resultsJSON");
    resultsObj = JSON.parse(results);
    if (resultsObj.great_price.length !== 0) {
      $(".results-table").empty();
      for (i = 0; i < resultsObj.great_price.length; i++) {
        $(".results-table").append(
          `<tr>
            <td>${resultsObj.great_price[i].year}</td>
            <td>${resultsObj.great_price[i].make}</td>
            <td>${resultsObj.great_price[i].model}</td>
            <td>${resultsObj.great_price[i].series}</td>
            <td>${resultsObj.great_price[i].mileage}</td>
          </tr>`
        );
      }
    }
  });

  $("#good-count").click(function () {
    // Retrieving data:
    results = localStorage.getItem("resultsJSON");
    resultsObj = JSON.parse(results);
    if (resultsObj.good_price.length !== 0) {
      $(".results-table").empty();
      for (i = 0; i < resultsObj.good_price.length; i++) {
        $(".results-table").append(
          `<tr>
            <td>${resultsObj.good_price[i].year}</td>
            <td>${resultsObj.good_price[i].make}</td>
            <td>${resultsObj.good_price[i].model}</td>
            <td>${resultsObj.good_price[i].series}</td>
            <td>${resultsObj.good_price[i].mileage}</td>
          </tr>`
        );
      }
    }
  });

  $("#fair-count").click(function () {
    // Retrieving data:
    results = localStorage.getItem("resultsJSON");
    resultsObj = JSON.parse(results);
    if (resultsObj.fair_price.length !== 0) {
      $(".results-table").empty();
      for (i = 0; i < resultsObj.fair_price.length; i++) {
        $(".results-table").append(
          `<tr>
            <td>${resultsObj.fair_price[i].year}</td>
            <td>${resultsObj.fair_price[i].make}</td>
            <td>${resultsObj.fair_price[i].model}</td>
            <td>${resultsObj.fair_price[i].series}</td>
            <td>${resultsObj.fair_price[i].mileage}</td>
          </tr>`
        );
      }
    }
  });

  $("#unknown-count").click(function () {
    // Retrieving data:
    results = localStorage.getItem("resultsJSON");
    resultsObj = JSON.parse(results);
    if (resultsObj.unknown.length !== 0) {
      $(".results-table").empty();
      for (i = 0; i < resultsObj.unknown.length; i++) {
        $(".results-table").append(
          `<tr>
            <td>${resultsObj.unknown[i].year}</td>
            <td>${resultsObj.unknown[i].make}</td>
            <td>${resultsObj.unknown[i].model}</td>
            <td>${resultsObj.unknown[i].series}</td>
            <td>${resultsObj.unknown[i].mileage}</td>
          </tr>`
        );
      }
    }
  });
});

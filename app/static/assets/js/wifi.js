/**
 * Created by harry on 6/30/16.
 */
$(document).ready(function() {
            $("#btnScanning").click(function() {
                var self = this;
                $(self).toggleClass("disabled");
                $(self).prop("disabled", true);
                $(self).text("Scanning ...");
                $.ajax(URL_WIFI_SCAN, {
                 "method" : "GET",
                  "success" : function (data) {
                      try {
                          var listSSID = data["ssid"];
                          console.log(listSSID);
                          $("#sel1").html("");
                          $.each(listSSID, function(index, val) {
                              $("#sel1").append("<option value='" + val + "'>"+ val +"</option>");
                          });
                          $(self).toggleClass("disabled");
                          $(self).text("Scan");
                          $(self).prop("disabled", false);
                      } catch(e) {
                          $(self).toggleClass("disabled");
                          $(self).text("Scan");
                          $(self).prop("disabled", false);
                      }

                  },
                  "error": function() {
                        $(self).toggleClass("disabled");
                        $(self).text("Scan");
                        $(self).prop("disabled", false);
                  }
                });
            });
 });

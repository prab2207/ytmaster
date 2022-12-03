var app=angular.module("appX",["ngSanitize"]);
app.controller("appCtrl",function($scope){
   $scope.greeting="Hello World";
   //$scope.darkmode=true;

   $scope.toggle = {};
   $scope.toggle.switch = false;
   $scope.openFile=function(content){
      window.open(
         sppath[$scope.clickedIndex],
         '_blank' // <- This is what makes it open in a new window.
       );
   }
   $scope.showPreview=function(content,highlightcontent){
      
      //$scope.previewcontent=resultcontent[content];
      //$scope.previewcontent=resultcontent[content-1];
      $scope.clickedIndex=content-1;
      //alert($("#result_content_"+content).html())
      var $div = $($("#result_content_"+content).html());
      //alert($div.find(".match").length)
      var htm=[]
      $div.find(".match").each(function(){
         //alert($(this).val())
         //alert(this.innerText);
         htm.push(this.innerText)
      })
      var words=unique(htm);

      //$("#loadpreviewcontent").attr("src",filepaths[content-1]);
      //document.getElementById("previewcontent").innerHTML='<object id="previewcontent_object" type="text/html" data="'+filepaths[content-1]+'" ></object>';
      //document.getElementById("previewcontent").innerHTML='<iframe  id="loadpreviewcontent" src="'+filepaths[content-1]+'" frameborder="0" marginheight="0" marginwidth="0" width="100%" style="height:100vh" scrolling="auto" ></iframe>';
      //document.getElementById("loadpreviewcontent").setAttribute("src",filepaths[content-1])
      $.ajax({         
         url: filepaths[content-1],      
         type: "GET",                   
         dataType: "html",                                 
         success: function (results) { 
            for(var i in words){
               var search_value=words[i]
               var search_regexp = new RegExp(search_value, "gi");
               results=results.replace(search_regexp,"<span class = 'highlight'>"+search_value+"</span>")
            }
            $("#contentprev").html(results);
         },//FIN SUCCES
         error: function(xhr, status, error){
            var errorMessage = xhr.status + ': ' + xhr.statusText
            $("#contentprev").html("<h1>unable to provide quick preview, please download the file</h1>");
            //alert('Error - ' + errorMessage);
        }
     
     });//FIN  AJAX

      $("#loadpreviewcontent").on("load", function() {
         let head = $("#loadpreviewcontent").contents().find("head");
         let css = '<style>/********* Put your styles here **********</style>';
         $(head).append(css);
       });
         setTimeout($scope.previewContentManip,2000)
      $(".Answers").each(function(){
         $(this).removeClass("active")
      })
      $(this).addClass("active");
      //highlightSearch();
      return;
      $('#id1 p').each(function() {
         var text = $(this).text();
         $(this).text(text.replace('dog', 'doll'));
       });
      var textarea = $('#previewcontent');    
      enew = textarea.html().replace(/(<mark>|<\/mark>)/igm, "");   
      alert(enew) 
      textarea.html(enew);     
          
      var query = new RegExp("("+queryVal+")", "gim");    
      newtext= textarea.html().replace(query, "<mark>$1</mark>");    
      newtext= newtext.replace(/(<mark>[^<>]*)((<[^>]+>)+)([^<>]*<\/mark>)/,"</mark><mark>");    

      textarea.html(newtext);  
     
   }
   $scope.previewContentManip=function(){
      $('#loadpreviewcontent').contents().find("html").html();

      //alert(document.getElementById('loadpreviewcontent').contentWindow.document.body.innerHTML)
      $('#previewcontent_object').load(function() {
         // find the element needed
         page = $('#previewcontent_object').contents();
         // alert to check
     });
   }
   $scope.convertToHTML=function(){
      var loadingTask = PDFJS.getDocument("/test.pdf");
      loadingTask.promise.then(
        function(pdf) {
          // Load information from the first page.
          pdf.getPage(1).then(function(page) {
            var scale = 1;
            var viewport = page.getViewport(scale);
      
            // Apply page dimensions to the <canvas> element.
            var canvas = document.getElementById("pdf");
            var context = canvas.getContext("2d");
            canvas.height = viewport.height;
            canvas.width = viewport.width;
      
            // Render the page into the <canvas> element.
            var renderContext = {
              canvasContext: context,
              viewport: viewport
            };
            page.render(renderContext).then(function() {
              console.log("Page rendered!");
            });
          });
        },
        function(reason) {
          console.error(reason);
        }
      );
   }
   });
   app.config(function($interpolateProvider) {
        $interpolateProvider.startSymbol('//').endSymbol('//');
    });


$(document).ready(function(){
   (function ($) {
      $.fn.replaceClass = function (pFromClass, pToClass) {
          return this.removeClass(pFromClass).addClass(pToClass);
      };


//check cookie for dark mode
$('.mode').replaceClass('whitemode','darkmode');
darkmodeval=$.cookie("luke_darkmode")
if(darkmodeval=="whitemode"){
   $('.mode').replaceClass('darkmode','whitemode');
   $("#darkmode").prop("checked", false)
}
else{
   $('.mode').replaceClass('whitemode','darkmode');
   $("#darkmode").prop("checked", true)
}


  }(jQuery));
   $('#darkmode').click(function(){
      if($(this).prop("checked") == true){
         $('.mode').replaceClass('whitemode','darkmode');
         $.cookie("luke_darkmode","darkmode")
      }
      else if($(this).prop("checked") == false){
         $('.mode').replaceClass('darkmode','whitemode');
         $.cookie("luke_darkmode","whitemode")
      }
   });
    $('.hover').tooltip({
        //title: "<div style='height:400px;width:400px><iframe src='https://www.google.com'></iframe></div>",
        title: fetchData,
        html: true,
     placement: 'right'
    });
  
    function fetchData()
    {
     var fetch_data = '';
     var element = $(this);
     var id = element.attr("id");
     $.ajax({
      url:"/results",
      method:"POST",
      async: false,
      data:{id:id},
      success:function(data)
      {
          //alert(data)
       fetch_data = data;
      }
     });   
     return fetch_data;
    }
   });
/*

   <div class="tooltip fade right in" role="tooltip" id="tooltip395273" style="top: 358.733px; left: 728px; display: block;"><div class="tooltip-arrow" style="top: 50%;"></div><div class="tooltip-inner">

   
*/
function highlightSearch() {
   var text = "sam";
   var query = new RegExp("(\\b" + text + "\\b)", "gim");
   var e = document.getElementById("previewcontent").innerHTML;
   return;
   var enew = e.replace(/(<span>|<\/span>)/igm, "");
   document.getElementById("previewcontent").innerHTML = enew;
   var newe = enew.replace(query, "<span>$1</span>");
   document.getElementById("previewcontent").innerHTML = newe;
   
 
 }

 window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("previewcontent");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    //header.classList.add("sticky");
  } else {
    //header.classList.remove("sticky");
  }
}

function unique(list) {
   var result = [];
   $.each(list, function(i, e) {
     if ($.inArray(e, result) == -1) result.push(e);
   });
   return result;
 }